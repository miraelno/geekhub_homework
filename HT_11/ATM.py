import datetime
import time

from db_connection import ConnectionDB
from exceptions import InvalidAddingAmountException
from exceptions import InvalidUsernameOrPasswordException
from exceptions import NotEnoughMoneyException
from exceptions import WrongValidationException
from queries import ADD_TRANSACTION
from queries import ADD_USER
from queries import SELECT_ALL_NOMINALS
from queries import SELECT_MINIMUM_NOMINAL
from queries import SELECT_TOTAL_BALANCE
from queries import SELECT_USER
from queries import UPDATE_NOMINAL_AMOUNT
from queries import UPDATE_USER_BALANCE
from utils import is_winner
from utils import take_value
from utils import validate_credentials
from user import User


class ATM:

    user = None

    def create_user(self, name: str, password: str):
        try:
            validate_credentials(name, password)
        except WrongValidationException as e:
            print(e)
            self.start()            

        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(ADD_USER, (name.lower(), password, 100 if is_winner() else 0, False))
            con.commit()

        print("Account was created!")

    def login(self, name: str, password: str):
        try:
            params = (name.lower(), password)
            with ConnectionDB() as con:
                cur = con.cursor()
                query_result = cur.execute(SELECT_USER, params)
                user_rows = query_result.fetchone()

            if not user_rows:
                raise InvalidUsernameOrPasswordException
            
        except InvalidUsernameOrPasswordException as e:
            print(e)
            self.start()

        self.user = User(
            user_rows['id'],
            user_rows['name'],
            user_rows['password'], 
            user_rows['balance'], 
            bool(user_rows['isCollector']),
            )
        
        print("Welcome to the system!")

    def add_balance(self, new_value: float):
        min_nominal = self.get_minimal_nominal()
        change = new_value % min_nominal

        if new_value < min_nominal:
            print(InvalidAddingAmountException())
            return

        if change > 0:
            print(f"Take your change: {change}")
            new_value = new_value - change
        
        self.user.balance += new_value
        params = (self.user.balance, self.user.id)

        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(UPDATE_USER_BALANCE, params)
            con.commit()

        self.add_transaction(new_value, "Top up at ATM")

    def add_transaction(self, transaction_value: float, transaction_description: str):
        params = (
            str(datetime.datetime.utcnow()),
            transaction_value,
            transaction_description,
            self.user.id,
        )

        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(ADD_TRANSACTION, params)
            con.commit()

    def withdraw_cash(self, amount: float):
        amount = float(amount)
        total_amount = self.get_total_amount()

        try:
            if self.user.balance < amount or total_amount < amount:
                raise NotEnoughMoneyException
        except NotEnoughMoneyException as e:
            print(e)
            return
        
        self.user.balance -= amount
        print(self.user.balance)
        input()
        params = (self.user.balance, self.user.id)

        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(UPDATE_USER_BALANCE, params)
            con.commit()

        self.add_transaction(amount, "Withdraw cash")
        print("The operation is successful!")

    def get_nominals(self):
        with ConnectionDB() as con:
            cur = con.cursor()
            query_result = cur.execute(SELECT_ALL_NOMINALS)
            nominals = query_result.fetchall()

        return nominals

    def change_nominal_amount(self):
        nominals = [row["nominal"] for row in self.get_nominals()]
        nominal = int(input("What nominal you want to change: ").strip())

        if nominal not in nominals:
            print("No such nominal.")
            return

        amount = int(input("Enter new value: ").strip())
        if amount < 0:
            print("You can't use negative value.")
            return

        with ConnectionDB() as con:
            cur = con.cursor()
            params = (amount, nominal)
            cur.execute(UPDATE_NOMINAL_AMOUNT, params)
            con.commit()

        print("The operation is successful!")

    def get_total_amount(self):
        with ConnectionDB() as con:
            cur = con.cursor()
            query_result = cur.execute(SELECT_TOTAL_BALANCE)
            row = query_result.fetchone()

        return row["balance"]

    def get_minimal_nominal(self):
        with ConnectionDB() as con:
            cur = con.cursor()
            cur.execute(SELECT_MINIMUM_NOMINAL)
            row = cur.fetchone()

        return row["min_nominal"]

    def collector_interaction(self):
        while True:
            answer = input(
                "1 - Show current nominal's amount\n2 - Change nominal's amount\n3 - Exit\n"
            ).strip()

            match answer:
                case "1":
                    nominals = self.get_nominals()
                    for row in nominals:
                        print(f"Nominal {row['nominal']} - {row['amount']}")
                case "2":
                    self.change_nominal_amount()
                case "3":
                    exit()
                case _:
                    print("No such option. Please, select one from the list.")

            time.sleep(1)

    def start_menu(self):
        answer = input("1 - Sign in\n2 - Sign up\n3 - Exit\n").strip()

        match answer:
            case "1":
                input_name = input(
                    "Hi! Please, enter your username without spaces: "
                ).strip()

                input_password = input("And your password: ").strip()

                return self.login(input_name, input_password)
            
            case "2":
                user_login = input(
                    "Enter your login. It should be from 3 to 50 symbols: "
                ).strip()
                user_password = input(
                    "Enter your password. It should be from 8 symbols and contain at least 1 digit: "
                ).strip()
                self.create_user(user_login, user_password)
            case "3":
                exit()
            case _:
                print("No such option.")

    def start(self):
        self.start_menu()

        if self.user.isCollector:
            self.collector_interaction()
            return

        while True:
            print("1 - My balance\n2 - Add balance\n3 - Withdraw cash\n4 - Exit\n")

            user_input = input("Select the operation by number: ").strip()

            match user_input:
                case "1":
                    print(self.user.balance)
                case "2":
                    value = take_value()

                    if value <= 0:
                        print("Negative value!")
                        continue

                    self.add_balance( value)
                    print("The operation is successful!")

                case "3":
                    value = take_value()
                    self.withdraw_cash(value)
                case "4":
                    print("Thank you for using our system!")
                    exit()
                case _:
                    print("No such option. Please, select one from the list.")

            time.sleep(1)