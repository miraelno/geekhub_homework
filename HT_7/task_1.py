# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль). Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException (його також треба створити =))
from exceptions import LoginException


def login(input_name=None, input_password=None, silent=False):
    users = [{'name': 'Ivan', 'password': '12345'},
             {'name': 'Viktoria', 'password': '4567'},
             {'name': 'Olha', 'password': 'Qwer123'},
             {'name': 'Polina', 'password': 'Rwq123'},
             {'name': 'Serhii', 'password': 'Lkj123'}]
    
    for i in users:
        if i['name'] == input_name and i['password'] == input_password:
            return True
    
    try:
        if silent is True:
            return False
        else:
            raise LoginException
    except LoginException as e:
        return e


print(login('Viktoria', '45675'))
