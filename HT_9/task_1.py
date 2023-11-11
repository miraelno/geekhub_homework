# 1. Програма-світлофор.
# Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора. 
# Кожну 1 секунду виводиться поточні кольори. 
# Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green
import time



def is_red(color):
    if color == 'Red':
        return True
    

while True:
    car = 'Red'

    for i in range(12):
        if i == 4:
            car = 'Yellow'
        elif i == 6:
            car = 'Green'
        elif i == 10:
            car = 'Yellow'
            
        pedestrian = 'Green' if is_red(car) else 'Red'

        print(f'{car} {pedestrian}')
        time.sleep(1)