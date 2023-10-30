# 2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
# обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
from exceptions import NotANumberException
from utils import convert_number


def difference(first_input, second_input):
    return first_input - second_input


def division(first_input, second_input):
    return first_input / second_input


def print_operations_results(first_input, second_input):
    try:
        first_input = convert_number(first_input)
        second_input = convert_number(second_input)
    except NotANumberException as e:
        return e
    
    print(f"The result of division is: {division(first_input, second_input)}")
    print(f"The result of difference is: {difference(first_input, second_input)}")


print(print_operations_results(10, 2))
