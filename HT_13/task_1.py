# 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
# завдання початкових розмірів об'єктів при їх створенні.

class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, new_color):
        self.color = new_color

class Oval(Figure):
    def __init__(self, perimeter):
        super().__init__()
        self.perimeter = perimeter

class Square(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

figure = Figure()
oval = Oval(20)
square = Square(10, 15)

print(figure.color)
print(oval.color)
print(square.color)

figure.change_color('yellow')
oval.change_color('blue')
square.change_color('black')

print(figure.color)
print(oval.color)
print(square.color)



