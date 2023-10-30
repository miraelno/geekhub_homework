# 5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити! 
# Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2). 
# Операції що мають бути присутні: +, -, *, /, %, //, **. 

def convert_number(num):
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            print('Not a number')


def calculator(user_input):
    first_operant, operator, second_operant = user_input.split(' ')

    first_operant = convert_number(first_operant)
    second_operant = convert_number(second_operant)

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
            print('Invalid input')


print(calculator(input()))
