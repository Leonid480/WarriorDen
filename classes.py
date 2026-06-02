from exceptions import DivisionByZeroError

class Math:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> float:
        return self.num1 + self.num2

    def subtract(self) -> float:
        return self.num1 - self.num2

    def multiply(self) -> float:
        return self.num1 * self.num2

    def divide(self) -> float:
        if self.num2 == 0:
            raise DivisionByZeroError()
        return self.num1 / self.num2
