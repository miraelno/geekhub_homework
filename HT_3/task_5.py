# 5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

test_dict = {'delete': 'duplicates', 'test': 'script', 'delete2': 'duplicates'}

result_dict = {}

for key, value in test_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value

print(result_dict)
