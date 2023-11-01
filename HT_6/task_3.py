# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні.

def is_prime(number):
    if 0 >= number >= 1000:
        return f"The number {number} isn't in range [0, 1000]."
    else:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                return False
        else:
            return True


print(is_prime(5))
