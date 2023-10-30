# 5. Ну і традиційно - калькулятор Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити! 
# Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2). 
# Операції що мають бути присутні: +, -, *, /, %, //, **. 
from exceptions import NotANumberException
from utils import convert_number


def calculator(user_input):
    try:
        first_operant, operator, second_operant = user_input.strip().split(' ')
    except Exception:
        print('Invalid input: valid format is "x ? y", where ? one of operants from the list: +, -, *, /, %, //, **')
        return
    
    try:
        first_operant = convert_number(first_operant)
        second_operant = convert_number(second_operant)
    except NotANumberException as e:
        return e

    match operator:
        case '+':
            return first_operant + second_operant
        case '-':
            return first_operant - second_operant
        case '*':
            return first_operant * second_operant
        case '/':
            return first_operant / second_operant
        case '%':
            return first_operant % second_operant
        case '//':
            return first_operant // second_operant
        case '**':
            return first_operant ** second_operant
        case _:
            print('Invalid operator')


result = calculator(input('Enter a formula in this format x + y:  '))
if result:
    print(result)
