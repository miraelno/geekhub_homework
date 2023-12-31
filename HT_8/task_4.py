# 4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) 
# і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент
#  із послідовності - ітерація починається знову.
#    Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#    for elem in generator([1, 2, 3]):
#        print(elem)
#    1
#    2
#    3
#    1
#    2
#    3
#    1
#    .......

def return_values(iterable_sequence):
    while True:
        for i in iterable_sequence:
            yield i


for i in return_values([1, 2, 3]):
    print(i)
          