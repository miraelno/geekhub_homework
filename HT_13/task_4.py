# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error. 
# Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи),
# але індексація повинна починатись із 1

class MyList(list):
    counter = 1




my_list = MyList(1)
print(my_list)
# print(my_list.index(None))
