class NotANumberException(Exception):

    def __init__(self, number):
        self.number = number
        super().__init__(self.number)

    def __str__(self):
        return f'{self.number} is not a number.'
