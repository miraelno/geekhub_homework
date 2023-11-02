# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона. 
# Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.
from utils import check_prime_number

def prime_list(start, end):

    if end < start:
        return "Invalid range numbers. Start greater than end."
    
    result_list = []
    try:
        if start < 0 or end < 0:
            return "Invalid range numbers."

        for number in range(start, end + 1):
            if check_prime_number(number):
                result_list.append(number)
    
    except TypeError:
        return "Invalid arguments type."

    return result_list


print(prime_list(0, 100))
