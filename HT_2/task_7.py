# 7. Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

list_to_concatenate = [2, 3, 'dsa', 'True', 76 , '5']

print(''.join(str(_) for _ in list_to_concatenate))