# 4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def process_the_string(string: str):
    string = string.replace(' ', '')
    print(len(string))
    if 30 <= len(string) <= 50:
        len_sum(string)
    elif len(string) < 30:
        sum_of_num(string)
    elif len(string) > 50:
        to_upper_case(string)


def len_sum(string: str):
    letters, numbers = find_num_and_symb(string)

    print(f"{len(letters)} letters in string")
    print(f"{len(numbers)} numbers in string")
    print(f"The length of the string is {len(string)}")


def sum_of_num(string: str):
    letters, numbers = find_num_and_symb(string)

    print(f'Sum of all numbers is: {sum(numbers)}')
    print(''.join(letters))


def to_upper_case(string: str):
    string_list, number_list = find_num_and_symb(string)

    for index, char in enumerate(string_list):
        if index % 2 == 0:
            string_list[index] = char.upper()

    print(''.join(string_list))


def find_num_and_symb(string):
    letters = []
    numbers = []

    for char in string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(int(char))
        else:
            print(char)

    return (letters, numbers)

process_the_string("f98neroi4nr0")
