# 7. Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

list_to_concatenate = [2,3,'dsa', 'True', 76, '5']
result_string = ''

for i in list_to_concatenate:
    result_string += str(i)

print(result_string)