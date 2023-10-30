# 4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def process_the_string(user_input: str):
    user_input_len = len(user_input)

    if 30 <= user_input_len <= 50:
        len_sum(user_input)
    elif user_input_len < 30:
        sum_of_num(user_input)
    elif user_input_len > 50:
        to_upper_case(user_input)


def len_sum(user_input: str):
    letters, numbers = find_num_and_symb(user_input)

    print(f"{len(letters)} letters in string")
    print(f"{len(numbers)} numbers in string")
    print(f"The length of the string is {len(user_input)}")


def sum_of_num(user_input: str):
    letters, numbers = find_num_and_symb(user_input)

    print(f'Sum of all numbers is: {sum(numbers)}')
    print(f"Result string: {''.join(letters)}")


def to_upper_case(user_input: str):
    string_list, _ = find_num_and_symb(user_input)

    for index, char in enumerate(string_list, 1):
        if index % 2 == 0:
            string_list[index - 1] = char.upper()

    print(f"Result string: {''.join(string_list)}")


def find_num_and_symb(user_input):
    letters = []
    numbers = []

    for char in user_input:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(int(char))

    return (letters, numbers)

process_the_string("f98ne roi4nr0jfkldsjf")
