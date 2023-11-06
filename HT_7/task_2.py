# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

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

def name_and_password_validation(name, password):
    for validation_regex, invalid_message in name_validators:
        if not re.match(validation_regex, name):
            raise WrongValidationException(invalid_message)

    for validation_regex, invalid_message in password_validators:
        if not re.match(validation_regex, password):
            raise WrongValidationException(invalid_message)

    return True


print(name_and_password_validation('         ', 'Qd'))
