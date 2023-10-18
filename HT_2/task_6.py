# 6. Write a script to check whether a value from user input is contained in a group of values.
#     e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

value_to_compare = [1, 2, 'u', 'a', 4, True]
value_from_user = input()

print(value_from_user in str(value_to_compare))