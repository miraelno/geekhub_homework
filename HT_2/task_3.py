# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number_from_user = int(input().strip())
result = 0

for i in range(1, number_from_user + 1):
    result += i

print(result)
