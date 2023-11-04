# 7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def count_same_elements(input_list: list):

    while len(input_list) > 0:
        counter = 1
        value = input_list.pop(0)
        for j in input_list:
            if isinstance(value, (dict, set, list, tuple)):
                if value == j:
                    input_list.remove(j)
                    counter += 1
            else:
                if value is j:
                    input_list.remove(j)
                    counter += 1
        print(f'{value} -> {counter}')



print(count_same_elements([1, 1, 'foo', (1, 2), [1, 2], 'foo', 1, [1, 2], 'True', True, {1, 2}, (1, 2)]))
