# 8. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

value_from_user = int(input().strip())

for _ in range(value_from_user):
    if _ % 17 == 0:
        print(_)