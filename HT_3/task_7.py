# 7. Write a script which accepts a <number> from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
#     e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

dict_size = int(input().strip())
result_dict = {}

for _ in range(dict_size):
    value_from_user = int(input().strip())
    result_dict[value_from_user] = value_from_user * value_from_user

print(result_dict)