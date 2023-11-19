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

from exceptions import (
    InvalidUsernameOrPasswordException, 
    NotEnoughMoneyException,
    InvalidAddingAmountException
)
from queries import (
    SELECT_USER,
    GET_USER_BALANCE,
    UPDATE_USER_BALANCE,
    ADD_TRANSACTION,
    ADD_USER
)
from utils import (
    take_value,
    get_connection,
    validate_credentials
)
from ConnectionDB import ConnectionDB


def create_user(name: str, password: str):
    validate_credentials(name, password)
    params = (name, password)

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(ADD_USER, params)
        con.commit()
        
    print('Account was created!')

def login(name: str, password: str):
    params = (name, password)
    con = get_connection()
    cur = con.cursor()
    user = cur.execute(SELECT_USER, params)
    user = user.fetchone()
    con.close()

    if not user:
        raise InvalidUsernameOrPasswordException
    
    print(f"Welcome to the system!")
    return list(user)


def get_balance(user: list):
    params = (user[0],)
    con = get_connection()
    cur = con.cursor()

    balance =  cur.execute(GET_USER_BALANCE, params)
    balance = balance.fetchone()
    con.close()


    return balance[0]


def add_balance(user: list, new_value: float):
    if new_value <= 0:
        raise InvalidAddingAmountException
    
    current_balance = user[3]
    params = (new_value + current_balance, user[0])

    with ConnectionDB() as con:
        cur = con.cursor()

        cur.execute(UPDATE_USER_BALANCE, params)
        con.commit()

    add_transaction(user, new_value, 'Top up at ATM')


def add_transaction(user: list, transaction_value: float, transaction_description: str):
    params = (str(datetime.datetime.utcnow()), transaction_value, transaction_description, user[0])

    with ConnectionDB() as con:
        cur = con.cursor()

        cur.execute(ADD_TRANSACTION, params)
        con.commit()


def withdraw_cash(user: list, amount: float):
    amount = float(amount)
    current_balance = get_balance(user)

    if current_balance < amount:
        raise NotEnoughMoneyException

    params = (current_balance - amount, user[0])

    with ConnectionDB() as con:
        cur = con.cursor()
        cur.execute(UPDATE_USER_BALANCE, params)
        con.commit()

    add_transaction(user, amount ,'Withdraw cash')

def collector_iteraction(collector):
    print('Hello collector')

def is_existing():
    answer = input("Hi! Do you have an account? Type 'y' or 'n': ").lower().strip()

    match answer:
        case 'y':
            return
        case 'n':
            user_login = input('Enter your login. It should be from 3 to 50 symbols: ')
            user_passwrod = input('Enter your password. It should be from 8 symbols and contain at least 1 digit: ')
            create_user(user_login, user_passwrod)
            return
        case _:
            print('No such option.')


def start():
    is_existing()

    input_name = input("Hi! Please, enter your username without speaces: ").strip()
    input_password = input("And your password: ").strip()

    logged_in_user = login(input_name, input_password)

    if logged_in_user[4]:
        collector_iteraction(logged_in_user)
        return

    while True:
        print("1 - My balance")
        print("2 - Add balance")
        print("3 - Withdraw cash")
        print("4 - Exit")

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
                print("The operation is successful!")
                
            case "4":
                print("Thank you for using our system!")
                return
            case _:
                print("No such option. Please, select one from the list.")

        time.sleep(1)

start()