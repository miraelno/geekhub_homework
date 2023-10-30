# 3. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
#     Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#     x > y;       вiдповiдь - "х бiльше нiж у на z"
#     x < y;       вiдповiдь - "у бiльше нiж х на z"
#     x == y.      вiдповiдь - "х дорiвнює z"
from exceptions import NotANumberException
from utils import convert_number

def check_equality(x, y):
    if x > y:
        print(f'{x} greater than {y} by {x - y}')
    elif x < y:
        print(f'{y} greater than {x} by {y - x}')
    elif x == y:
        print(f'{x} is equal to {y}')


try:
    x = convert_number(input('Enter first number: '))
    y = convert_number(input('Enter second number: '))
except NotANumberException as e:
    print(e)
else:
    check_equality(x, y)
