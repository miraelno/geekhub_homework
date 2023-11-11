class NotEnoughSymbolsException(Exception):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return f'Not enough symbols in file. Please, select another file or enter less symbols.'


# class WrongValidationException(Exception):

#     def __init__(self, message):
#         super().__init__(self)
#         self.message = message

#     def __str__(self):
#         return self.message
