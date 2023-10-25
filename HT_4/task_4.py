# Write a Python program that demonstrates exception chaining. Create a custom exception class called CustomError and another called SpecificError. 
# In your program (could contain any logic you want), raise a SpecificError, and then catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause. 
# Display both the custom error message and the original exception message.

class CustomError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return f'Custom error'


class SpecificError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return f'Specific error'


try:
    try:
        print(2 / 2)
        raise SpecificError
    except SpecificError as e:
        raise CustomError from e
except CustomError as e:
    print(e.__context__)
    print(e)
