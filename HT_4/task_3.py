# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise a custom exception called InvalidAgeError. 
# Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeError(Exception):
    age: int

    def __init__(self, age):
        self.age = age
        super().__init__(self.age)
    
    def __str__(self):
        return f'The entered {self.age} isn\'t in range [18, 120]'


def check_the_age():
    age = int(input())
    try:
        if age < 18 or age > 120:
            raise InvalidAgeError(age)
    except InvalidAgeError as e:
        print(e)
    

check_the_age()