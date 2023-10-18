# 1. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

user_input = input().strip().split(',')

print(user_input)
print(tuple(user_input))