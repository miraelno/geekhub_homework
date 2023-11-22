class InvalidUsernameOrPasswordException(Exception):
    def __str__(self):
        return "Invalid name and/or password."


class NotEnoughMoneyException(Exception):
    def __str__(self):
        return "Not enough money for this operation."


class InvalidAddingAmountException(Exception):
    def __str__(self):
        return "You can't put less that minimal nominal."


class WrongValidationException(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message
