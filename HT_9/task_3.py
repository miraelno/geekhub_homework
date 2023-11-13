# 3. Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій
import csv
import datetime
import json
import time

from exceptions import InvalidUsernameOrPasswordException, NotEnoughMoneyException

from enums import FileTypes
from utils import find_file, take_value


def login(name, password):
    users_file = find_file(FileTypes.USER)

    with open(users_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            if line[0].lower() == name.lower() and line[1] == password:
                print(f'Welcome to the system!')
                return name
            else:
                raise InvalidUsernameOrPasswordException


def getBalance(user_name: str):
    balance_file = find_file(FileTypes.BALANCE, user_name)

    with open(balance_file, 'r') as f:
        user_balance = f.readline()
        return float(user_balance)


def updateBalance(user_name: str, new_value: float):
    balance_file = find_file(FileTypes.BALANCE, user_name)

    with open(balance_file, 'w') as f:
        f.write(str(new_value))


def addTransaction(user_name: str, transaction_data: dict):
    transactions_file = find_file(FileTypes.TRANSACTION, user_name)

    with open(transactions_file, 'r+') as f:
        data = json.load(f)
        data['transactions'].append(transaction_data)
        f.seek(0)
        json.dump(data, f, indent=2)


def withdraw_cash(user_name: str, amount: float):
    amount = float(amount)
    balance = getBalance(user_name)

    if balance < amount:
        raise NotEnoughMoneyException

    transaction_data = {
        "date": str(datetime.datetime.now()),
        "amount": amount,
        "description": "Withdraw cash"
    }

    updateBalance(user_name, balance - amount)
    addTransaction(user_name, transaction_data)


def start():

    input_name = input(
        'Hi! Please, enter your username without speaces: ').strip()
    input_password = input('And your password: ').strip()

    logged_in_user = login(input_name, input_password)

    if logged_in_user:

        while True:
            print('1 - My balance')
            print('2 - Add balance')
            print('3 - Withdraw cash')
            print('4 - Exit')

            user_input = input('Select the operation by number: ').strip()
            current_balance = getBalance(input_name)

            match user_input:
                case '1':
                    print(current_balance)
                case '2':
                    value = take_value()
                    updateBalance(input_name, value + current_balance)
                    print('The operation is successful!')

                    transaction_data = {
                        "date": str(datetime.datetime.now()),
                        "amount": value,
                        "description": "Replenishment at an ATM"
                    }
                    addTransaction(input_name, transaction_data)
                case '3':
                    while True:
                        value = take_value()
                        if current_balance >= value:
                            break
                        else:
                            print('Not enough money. Try again.')

                    updateBalance(input_name, current_balance - value)
                    print('The operation is successful!')

                    transaction_data = {
                        "date": str(datetime.datetime.now()),
                        "amount": value,
                        "description": "Withdrawing cash from an ATM"
                    }
                    addTransaction(input_name, transaction_data)
                case '4':
                    print('Thank you for using our system!')
                    return
                case _:
                    print('No such option. Please, select one from the list.')

            time.sleep(1)


start()
