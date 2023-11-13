class NotEnoughSymbolsException(Exception):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return f'Not enough symbols in file. Please, select another file or enter less symbols.'


class InvalidUsernameOrPasswordException(Exception):

    def __init__(self):
        super().__init__(self)


    def __str__(self):
        return 'Invalid name and/or password.'
    

class NotEnoughMoneyException(Exception):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Not enough money for this operation.'

