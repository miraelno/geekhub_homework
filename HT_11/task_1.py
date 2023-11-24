# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...
# - Додати документування в клас (можете почитати цю статтю:
# https://realpython.com/documenting-python-code/ )


class Calc:
    """
    This class perform math operations with 2 numbers.
    It has 4 methods: add(), subtraction(), multiplication() and division().
    It also has last_result attribut witch store a result of previous math operation.
    """

    last_result = None
    current_result = None

    def add(self, a: int | float, b: int | float) -> int | float:
        """This method performs adding with 2 numbers."""
        self.last_result = self.current_result

        result = a + b
        self.current_result = result
        return result

    def subtraction(self, a: int | float, b: int | float) -> int | float:
        """This method performs subtraction with 2 numbers."""
        self.last_result = self.current_result

        result = a - b
        self.current_result = result
        return result

    def multiplication(self, a: int | float, b: int | float) -> int | float:
        """This method performs multiplication with 2 numbers."""
        self.last_result = self.current_result

        result = a * b
        self.current_result = result
        return result

    def division(self, a: int | float, b: int | float) -> int | float:
        """This method performs division with 2 numbers."""
        self.last_result = self.current_result

        result = a / b
        self.current_result = result
        return result


calc = Calc()

print(calc.last_result)
calc.add(2, 3)
print(calc.last_result)
calc.division(2, 1)
print(calc.last_result)
calc.add(2, 9)
print(calc.last_result)
