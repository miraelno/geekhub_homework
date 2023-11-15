# 2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій.
# На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або,
#  наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?).
#  Не забудьте додати перевірку чи файл існує.

from exceptions import NotEnoughSymbolsException
from math import ceil


def print_symbols(file_path, size_to_print):
    try:
        with open(file_path, 'r') as f:
            file_data = f.read()
    except FileNotFoundError:
        print('No such file or wrong path.')
        return

    file_data_len = len(file_data)
    if file_data_len < size_to_print:
        raise NotEnoughSymbolsException
    if (file_data_len - size_to_print) % 2 != 0:
        raise NotEnoughSymbolsException

    center = ceil(file_data_len / 2) - ceil(size_to_print / 2)
    print([
        file_data[:size_to_print],
        file_data[center:center + size_to_print],
        file_data[-size_to_print:]
    ])


print_symbols('test_file.txt', 3)
