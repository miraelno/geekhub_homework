# 1. Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

tuple_1 = (1, 2, 3)
tuple_2 = ('1', '2', '3', '4')
tuple_3 = ('test', [1, 2, 3], True, 'hello', [True, False])

list_of_tuples = [tuple_1, tuple_2, tuple_3]
value_from_user = input()

for i in list_of_tuples:
    i = list(i)
    print(f"Last value before change {i[-1]}")
    i[-1] = value_from_user
    print(f"Last value after change {i[-1]}")
    i = tuple(i)

print(tuple_1)