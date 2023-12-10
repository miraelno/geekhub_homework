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
from queries import SELECT_USER_BALANCE
from queries import UPDATE_NOMINAL_AMOUNT
from queries import UPDATE_USER_BALANCE
from utils import take_value
from utils import validate_credentials


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
            print(user['id'])
        if not user:
            raise InvalidUsernameOrPasswordException

    except InvalidUsernameOrPasswordException as e:
        print(e)
        start()

    print("Welcome to the system!")

    return user


def get_balance(user):
    params = (user["id"],)
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(SELECT_USER_BALANCE, params)
        row = query_result.fetchone()

    return row["balance"]


def add_balance(user, new_value: float):
    min_nominal = get_minimal_nominal()
    change = new_value % min_nominal

    if new_value < min_nominal:
        print(InvalidAddingAmountException())
        return

    if change > 0:
        print(f"Take your change: {change}")

    new_value = new_value - change
    current_balance = get_balance(user)
    params = (new_value + current_balance, user["id"])

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(UPDATE_USER_BALANCE, params)
        con.commit()

    add_transaction(user, new_value, "Top up at ATM")


def add_transaction(user, transaction_value: float, transaction_description: str):
    params = (
        str(datetime.datetime.utcnow()),
        transaction_value,
        transaction_description,
        user["id"],
    )

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(ADD_TRANSACTION, params)
        con.commit()


def withdraw_cash(user, amount: float):

    amount = float(amount)
    current_balance = get_balance(user)
    total_amount = get_total_amount()

    try:
        if current_balance < amount or total_amount < amount:
            raise NotEnoughMoneyException
    except NotEnoughMoneyException as e:
        print(e)
        return

    params = (current_balance - amount, user["id"])

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
    nominals = [row["nominal"] for row in get_nominals()]
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


def get_total_amount():
    with ConnectionDB() as con:
        cur = con.cursor()
        query_result = cur.execute(SELECT_TOTAL_BALANCE)
        row = query_result.fetchone()

    return row["balance"]


def get_minimal_nominal():
    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(SELECT_MINIMUM_NOMINAL)
        row = cur.fetchone()

    return row["min_nominal"]


def collector_iteraction():
    while True:
        answer = input(
            "1 - Show current nominal's amount\n2 - Change nominal's amount\n3 - Exit\n"
        ).strip()

        match answer:
            case "1":
                nominals = get_nominals()
                for row in nominals:
                    print(f"Nominal {row['nominal']} - {row['amount']}")
            case "2":
                change_nominal_amount()
            case "3":
                exit()
            case _:
                print("No such option. Please, select one from the list.")

        time.sleep(1)


def start_menu():
    answer = input("1 - Sign in\n2 - Sign up\n3 - Exit\n").strip()

    match answer:
        case "1":
            input_name = input(
                "Hi! Please, enter your username without speaces: "
            ).strip()
            input_password = input("And your password: ").strip()

            return login(input_name, input_password)
        case "2":
            user_login = input(
                "Enter your login. It should be from 3 to 50 symbols: "
            ).strip()
            user_passwrod = input(
                "Enter your password. It should be from 8 symbols and contain at least 1 digit: "
            ).strip()
            create_user(user_login, user_passwrod)
        case "3":
            exit()
        case _:
            print("No such option.")


def start():
    logged_in_user = None

    while not logged_in_user:
        logged_in_user = start_menu()

    print(logged_in_user["id"])
    if logged_in_user["isCollector"]:
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


if __name__ == "__main__":
    start()
