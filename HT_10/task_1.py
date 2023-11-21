#  - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
#     - на старті додати можливість залогінитися або створити новго користувача (при створенні новго користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
#     - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)
import datetime
import time

from ConnectionDB import ConnectionDB
from exceptions import (
    InvalidUsernameOrPasswordException,
    NotEnoughMoneyException,
    InvalidAddingAmountException,
    WrongValidationException
)
from queries import (
    SELECT_USER,
    GET_USER_BALANCE,
    UPDATE_USER_BALANCE,
    ADD_TRANSACTION,
    ADD_USER,
    SELECT_ALL_NOMINALS,
    UPDATE_NOMINAL,
    SELECT_NOMINAL_ID,
    SELECT_TOTAL_BALANCE,
    SELECT_MINIMUM_NOMINAL,
)
from utils import take_value, validate_credentials


def create_user(name: str, password: str):
    try:
        validate_credentials(name, password)
    except WrongValidationException as e:
        print(e)
        start()

    params = (name.lower(), password)

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(ADD_USER, params)
        con.commit()

    print("Account was created!")


def login(name: str, password: str):
    try:
        params = (name.lower(), password)
        with ConnectionDB() as con:
            cur = con.cursor()
            query_result = cur.execute(SELECT_USER, params)
            user = query_result.fetchone()
        
        if not user:
            raise InvalidUsernameOrPasswordException
        
    except InvalidUsernameOrPasswordException as e:
        print(e)
        start()

    print("Welcome to the system!")
    return list(user)


def get_balance(user: list):
    params = (user[0],)
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(GET_USER_BALANCE, params)
        balance = query_result.fetchone()

    return balance[0]


def add_balance(user: list, new_value: float):
    min_nominal = get_minimal_nominal()
    change = new_value % min_nominal

    try:
        if new_value < min_nominal:
            raise InvalidAddingAmountException
    except InvalidAddingAmountException as e:
        print(e)
        return
    
    if change > 0:
        print(f"Take your change: {change}")

    new_value = new_value - change

    current_balance = user[3]
    params = (new_value + current_balance, user[0])

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(UPDATE_USER_BALANCE, params)
        con.commit()

    add_transaction(user, new_value, "Top up at ATM")


def add_transaction(user: list, transaction_value: float, transaction_description: str):
    params = (
        str(datetime.datetime.utcnow()),
        transaction_value,
        transaction_description,
        user[0],
    )

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(ADD_TRANSACTION, params)
        con.commit()


def withdraw_cash(user: list, amount: float):

    amount = float(amount)
    current_balance = get_balance(user)
    total_amount = get_total_amount()

    try:
        if current_balance < amount or total_amount < amount:
            raise NotEnoughMoneyException
    except NotEnoughMoneyException as e:
        print(e)
        return
    
    params = (current_balance - amount, user[0])

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(UPDATE_USER_BALANCE, params)
        con.commit()

    add_transaction(user, amount, "Withdraw cash")
    print("The operation is successful!")


def get_nominals():
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(SELECT_ALL_NOMINALS)
        nominals = query_result.fetchall()
        return nominals


def change_nominal_amount():
    nominals = [i[1] for i in get_nominals()]
    nominal = int(input("What nominal you want to change?: ").strip())

    if nominal not in nominals:
        print('No such nominal.')
        return
    
    amount = int(input("Enter new value: ").strip())
    if amount < 0:
        print("You can't user negative value.")
        return
    
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(SELECT_NOMINAL_ID, (nominal,))
        nominal_id = query_result.fetchone()

        params = (amount, nominal_id[0])
        cur.execute(UPDATE_NOMINAL, params)
        con.commit()

    print("The operation is successful!")


def get_total_amount():
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(SELECT_TOTAL_BALANCE)
        total_amount = query_result.fetchone()
        return total_amount[0]


def get_minimal_nominal():
    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(SELECT_MINIMUM_NOMINAL)
        result = cur.fetchone()
        return result[0]


def collector_iteraction():
    while True:
        answer = input("1 - Show current nominal's amount\n2 - Change nominal's amount\n3 - Exit\n").strip()

        match answer:
            case "1":
                nominals = get_nominals()
                for i in nominals:
                    print(f"Nominal {i[1]} - {i[2]}")
            case "2":
                change_nominal_amount()
            case "3":
                return
            case _:
                print("No such option. Please, select one from the list.")
        time.sleep(1)

def is_existing():
    while True:
        answer = input("1 - Sign in \n2 - Sign up\n3 - Exit\n").strip()

        match answer:
            case "1":
                return
            case "2":
                user_login = input(
                    "Enter your login. It should be from 3 to 50 symbols: "
                ).strip()
                user_passwrod = input(
                    "Enter your password. It should be from 8 symbols and contain at least 1 digit: "
                ).strip()
                create_user(user_login, user_passwrod)
                return
            case "3":
                exit()
            case _:
                print("No such option.")


def start():

    is_existing()

    input_name = input("Hi! Please, enter your username without speaces: ").strip()
    input_password = input("And your password: ").strip()

    logged_in_user = login(input_name, input_password)

    if logged_in_user[4]:
        collector_iteraction()
        return

    while True:
        print("1 - My balance\n2 - Add balance\n3 - Withdraw cash\n4 - Exit\n")

        user_input = input("Select the operation by number: ").strip()

        match user_input:
            case "1":
                print(get_balance(logged_in_user))
            case "2":
                value = take_value()

                if value <= 0:
                    print("Negative value!")
                    continue

                add_balance(logged_in_user, value)
                print("The operation is successful!")

            case "3":
                value = take_value()
                withdraw_cash(logged_in_user, value)
            case "4":
                print("Thank you for using our system!")
                exit()
            case _:
                print("No such option. Please, select one from the list.")

        time.sleep(1)


start()
