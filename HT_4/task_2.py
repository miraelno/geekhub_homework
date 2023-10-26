# Create a custom exception class called NegativeValueError. 
# Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative. 
# Handle this custom exception with a try/except block and display an error message.

class NegativeValueError(Exception):
    number: int

    def __init__(self, number):
        self.number = number
        super().__init__(self.number)
    
    def __str__(self):
        return f'Number {self.number} in negative'


def negative_value_check(number):
    try:
        if number < 0:
            raise NegativeValueError(number)
    except NegativeValueError as e:
        print(f"Error: {e}")


negative_value_check(int(input('Enter a number: ')))
