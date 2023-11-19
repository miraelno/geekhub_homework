#  - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
#     - на старті додати можливість залогінитися або створити новго користувача (при створенні новго користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
#     - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)

import sqlite3
import csv
import datetime
import json
import time

from exceptions import InvalidUsernameOrPasswordException, NotEnoughMoneyException

# from utils import find_file, take_value

con = sqlite3.connect("ATM_DB.db")
cur = con.cursor()


# def login(name, password):
#     users_file = find_file(FileTypes.USER)

#     with open(users_file, "r") as csv_file:
#         csv_reader = csv.reader(csv_file)

#         next(csv_reader)

#         for line in csv_reader:
#             if line[0].lower() == name.lower() and line[1] == password:
#                 print(f"Welcome to the system!")
#                 return name
#             else:
#                 raise InvalidUsernameOrPasswordException


# def get_balance(user_name: str):
#     balance_file = find_file(FileTypes.BALANCE, user_name)

#     with open(balance_file, "r") as f:
#         user_balance = f.readline()
#         return float(user_balance)


# def update_balance(user_name: str, new_value: float):
#     balance_file = find_file(FileTypes.BALANCE, user_name)

#     with open(balance_file, "w") as f:
#         f.write(str(new_value))


# def add_transaction(user_name: str, transaction_data: dict):
#     transactions_file = find_file(FileTypes.TRANSACTION, user_name)

#     with open(transactions_file, "r+") as f:
#         data = json.load(f)
#         data["transactions"].append(transaction_data)
#         f.seek(0)
#         json.dump(data, f, indent=2)


# def withdraw_cash(user_name: str, amount: float):
#     amount = float(amount)
#     balance = get_balance(user_name)

#     if balance < amount:
#         raise NotEnoughMoneyException

#     transaction_data = {
#         "date": str(datetime.datetime.now()),
#         "amount": amount,
#         "description": "Withdraw cash",
#     }

#     update_balance(user_name, balance - amount)
#     add_transaction(user_name, transaction_data)


# def start():

#     input_name = input("Hi! Please, enter your username without speaces: ").strip()
#     input_password = input("And your password: ").strip()

#     logged_in_user = login(input_name, input_password)

#     if logged_in_user:

#         while True:
#             print("1 - My balance")
#             print("2 - Add balance")
#             print("3 - Withdraw cash")
#             print("4 - Exit")

#             user_input = input("Select the operation by number: ").strip()
#             current_balance = get_balance(input_name)

#             match user_input:
#                 case "1":
#                     print(current_balance)
#                 case "2":
#                     value = take_value()
#                     if value <= 0:
#                         print("Negative value!")
#                         continue

#                     update_balance(input_name, value + current_balance)
#                     print("The operation is successful!")

#                     transaction_data = {
#                         "date": str(datetime.datetime.now()),
#                         "amount": value,
#                         "description": "Replenishment at an ATM",
#                     }
#                     add_transaction(input_name, transaction_data)
#                 case "3":
#                     while True:
#                         value = take_value()
#                         if current_balance >= value:
#                             break
#                         else:
#                             print("Not enough money. Try again.")

#                     update_balance(input_name, current_balance - value)
#                     print("The operation is successful!")

#                     transaction_data = {
#                         "date": str(datetime.datetime.now()),
#                         "amount": value,
#                         "description": "Withdrawing cash from an ATM",
#                     }
#                     add_transaction(input_name, transaction_data)
#                 case "4":
#                     print("Thank you for using our system!")
#                     return
#                 case _:
#                     print("No such option. Please, select one from the list.")

#             time.sleep(1)


# start()
result = cur.execute("SELECT balance FROM users WHERE id = 1")
print(result.fetchall())
