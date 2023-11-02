# 7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньомy і виводить результат. 
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
from collections import Counter


 
def count_same_elements(input_list):
    return Counter(input_list)
#   unique_l = []

#   for i in input_list:
#     if i not in unique_l:
#       unique_l.append(i)

#   for i in unique_l:
#     print(f'{i} -> {input_list.count(i)}')

print(count_same_elements([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))


# def fun(l):
#     handled_keys = []

#     for i in l:
#         for j in handled_keys:
#             if j != i or type(j) != type(i):
#                 count = 0
#                 for j in l:
#                     if j == i and type(j) == type(i):
#                         count += 1
#                         print(i, count)
#                         handled_keys.append(i)
#                         result = Counter(l)
                        

# print(fun([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))