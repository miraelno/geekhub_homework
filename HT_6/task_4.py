# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона. 
# Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.

def prime_list(start, end):

    result_list = []
    try:
        if start < 0 or end < 0:
            return "Invalid range numbers."

        for number in range(start, end + 1):
            if number < 2:
                continue
            else:
                for i in range(2, int(number ** 0.5 + 1)):
                    if number % i == 0:
                        break
                else:
                    result_list.append(number)
    except TypeError:
        return "Invalid arguments type."

    return result_list


print(prime_list(5, 100))