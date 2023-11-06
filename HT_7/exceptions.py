class LoginException(Exception):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return f'Invalid name or/and password.'


class WrongValidationException(Exception):

    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message
