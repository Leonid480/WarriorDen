class CalculationError(Exception):
    """Базовый класс для ошибок калькулятора."""
    pass

class DivisionByZeroError(CalculationError):
    """Ошибка, возникающая при делении на ноль."""
    def __init__(self, message="Деление на ноль недопустимо."):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(CalculationError):
    """Ошибка, возникающая при вводе некорректных данных."""
    def __init__(self, message="Введены некорректные данные. Ожидаются числа."):
        self.message = message
        super().__init__(self.message)
