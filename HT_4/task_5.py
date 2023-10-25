# Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. 
# Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered. 
# Display the final valid integer.

number = input('Enter a number: ')
while True:
    try:
        print(int(number))
    except ValueError:
        number = input('Please, try again: ')
    else:
        break
