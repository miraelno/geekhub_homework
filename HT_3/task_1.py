# 1. Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

tuple_1 = (1, 2, 3)
tuple_2 = ('1', '2', '3', '4')
tuple_3 = ('test', [1, 2, 3], True, 'hello', [True, False])
tuple_4 = ()

list_of_tuples = [tuple_1, tuple_2, tuple_3, tuple_4]
value_from_user = input()

print(list_of_tuples)
for index, value in enumerate(list_of_tuples):
    if not value:
        continue
    new_tuple = list(value)
    new_tuple[-1] = value_from_user
    value = tuple(new_tuple)
    list_of_tuples[index] = value

print(list_of_tuples)
