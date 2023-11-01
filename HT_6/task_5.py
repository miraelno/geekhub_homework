# 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(limit, a=0, b=1):
    
    if a <= limit:
        print(a)
        fibonacci(limit, b, a + b)
        
    
fibonacci(5)
