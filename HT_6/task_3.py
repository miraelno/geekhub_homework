# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні.
from utils import check_prime_number


def is_prime(number):
    if 0 >= number >= 1000:
        return f"The number {number} isn't in range [0, 1000]."
    
    return check_prime_number(number)


print(is_prime(2))
