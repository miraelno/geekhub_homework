# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи, які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession (його не має інсувати під час ініціалізації).


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        print(f"My name is {self.name}. I am {self.age} old.")


person_1 = Person("John", 21)
person_2 = Person("Jake", 30)

person_1.profession = "financier"
print(person_1.profession)

person_2.profession = "waiter"
print(person_2.profession)
