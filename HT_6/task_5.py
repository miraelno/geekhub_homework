# 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(limit):
    a = 1  
    b = 0  
    print (b)
    print(a)

    while (a < limit):
        c = b  
        b = a  
        a = c + b  
        print(a) 
         
fibonacci(5)
