# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float, а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення


def check_number():
    number = input('Enter a number: ')
    while True:
        try:
            return int(number)
        except ValueError:
            try:
                return float(number)
            except ValueError:
                number = input('Please, try again: ')
        

numbers = [check_number(), check_number()]

try:
    print(numbers[0] / numbers[1])
except Exception as e:
    print(f'Something went wrong: {e}')
