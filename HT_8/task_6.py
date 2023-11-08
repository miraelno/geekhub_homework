# 6. Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова. 
# Реалізуйте обчислення за допомогою генератора.


value = 'dsdas dasdas snfkds dsa'

def check_len(string):
    words = string.split(' ')
    
    result = min(len(word) for word in words)
    yield result


for i in check_len(value):
    print(i)