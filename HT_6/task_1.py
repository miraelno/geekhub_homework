# 1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.

def square(square_side):

    if isinstance(square_side, (float, int)):
        return square_side * 4, square_side ** 2, square_side * (2 ** 0.5)
    return "Invalid value. Provide a number."


print(square(3.5))
