# 3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)

import re

from exceptions import WrongValidationException

name_validators = [
    (r"\w{3,50}", "Invalid name length"),
]
password_validators = [
    (r"\w{8,}", "Invalid password length"),
    (r"^[A-Z]{1}", "Password must starts with upper character"),
    (r"\w*\d+\w*", "Must contain at least 1 digit"),
]

users = [
    {'name': 'Ivan', 'password': '12345'},
    {'name': 'Vi', 'password': 'Qwer1234'},
    {'name': 'OlhadsadasdOlhadsadasdOlhadsadasdOlhadsadasdOlhadsadasdOlh', 'password': 'qwer123'},
    {'name': 'Polina123', 'password': 'Rwq1'},
    {'name': 'Serhii', 'password': 'Lkj123sad'},
]


def name_and_password_validation(name, password):
    for validation_regex, invalid_message in name_validators:
        if not re.match(validation_regex, name):
            raise WrongValidationException(invalid_message)

    for validation_regex, invalid_message in password_validators:
        if not re.match(validation_regex, password):
            raise WrongValidationException(invalid_message)

    return True


for user in users:
    print(f"Name: {user['name']}")
    print(f"Password: {user['password']}")
    try:
        name_and_password_validation(user['name'], user['password'])
    except WrongValidationException as e:
        print(f"Status: {e}")
    else:
        print(f"Status: OK")
    print("-------")
