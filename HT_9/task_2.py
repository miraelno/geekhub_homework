# 2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій.
# На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або,
#  наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?).
#  Не забудьте додати перевірку чи файл існує.

from exceptions import NotEnoughSymbolsException


def print_symbols(file_path=None, size_to_print=None):
    try:
        file_size = validate_size(file_path, size_to_print)
    except FileNotFoundError:
        print('No such file or wrong path.')
        return 
    
    blocks_size = file_size // 3


    with open(file_path, 'r') as f:

        for block in range(1, 4):
            f_to_print = f.read(blocks_size)
            print(f'{"-"*8}Symbols from {block} block{"-"*8}')
            print(f_to_print[:size_to_print])



def validate_size(file_path, size_to_print):

    with open(file_path, 'r') as f:
        f_content = f.read()

        file_number_of_symbols = len(f_content)

        if file_number_of_symbols < size_to_print or file_number_of_symbols < (size_to_print * 3):
            raise NotEnoughSymbolsException
    return file_number_of_symbols

print_symbols('test_file.txt', 100)
