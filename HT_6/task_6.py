# 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
# Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def shift_elements(input_list, shift):

    if shift == 0:
        return input_list
    
    elif shift > 0:
        for _ in range(shift):
            p = input_list.pop()
            input_list.insert(0, p)
            
    elif shift < 0:
        for _ in range(abs(shift)):
            p = input_list.pop(0)
            input_list.append(p)

    return input_list

print(shift_elements([1, 2, 3, 4, 5], -2))