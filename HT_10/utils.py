import sqlite3
import re

from exceptions import WrongValidationException


def take_value():
    try:
        user_input = input("Enter a value: ")
        user_input = float(user_input)
        return user_input
    except ValueError:
        print("Please, enter a valid number!")

def get_connection():
    return sqlite3.connect("ATM_DB.db")

def validate_credentials(name, password):
    
    name_validators = [
    (r"\w{3,50}", "Invalid name length"),
    ]

    password_validators = [
    (r"\w{8,}", "Invalid password length"),
    (r"\w*\d+\w*", "Must contain at least 1 digit"),
    ]

    for validation_regex, invalid_message in name_validators:
        if not re.match(validation_regex, name):
            raise WrongValidationException(invalid_message)

    for validation_regex, invalid_message in password_validators:
        if not re.match(validation_regex, password):
            raise WrongValidationException(invalid_message)

    return True