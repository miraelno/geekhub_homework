import os
from enums import FileTypes

from pathlib import Path


def find_file(file_type: FileTypes, username=None):
    if file_type is FileTypes.USER:
        return 'bankomat_DB/users.csv'

    if username is None:
        return 'For finding balance or transactions files you should add a username.'

    list_of_files = os.listdir(f'bankomat_DB/{file_type.value}')
    for_user = [i for i in list_of_files if i.startswith(
        username.lower().strip())]
    if len(for_user) > 1:
        return 'More than 1 files are found. Please, specify the user name.'
    elif len(for_user) == 0:
        return 'No data is found'
    else:
        return f'bankomat_DB/{file_type.value}/{for_user[0]}'


def take_value():
    while True:
        try:
            user_input = input('Enter a value: ')
            user_input = float(user_input)
            return user_input
        except ValueError:
            print('Please, enter a valid number!')
