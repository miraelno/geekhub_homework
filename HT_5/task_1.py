# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь). 
# У випадку некоректного введеного значення - виводити відповідне повідомлення.

def season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        print("There is no such month")

month = int(input("Enter the number: "))
result = season(month)
print(f"Returned value - {result}")
