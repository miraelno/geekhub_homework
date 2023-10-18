# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.

counter = int(input().strip())
result_string = ''

for i in range(counter):
    result_string += input()

print(result_string)