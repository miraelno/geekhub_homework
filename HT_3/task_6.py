# 6. Write a script to get the maximum and minimum value in a dictionary.

test_dict = {'middle1': 11, 'max': 20, 'min': 1, 'middle2': 15, 'middle3': [], 'middle4': '13'}

values = list(filter(lambda x: isinstance(x, int), test_dict.values()))
print(f"The max value is: {max(values)}")
print(f"The min value is: {min(values)}")

print(test_dict.values())
