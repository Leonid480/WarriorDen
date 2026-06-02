from exceptions import InvalidInputError

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с валидацией ввода."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            raise InvalidInputError("Пожалуйста, введите корректное числовое значение.")

def get_operation() -> str:
    """Запрашивает у пользователя знак операции."""
    valid_operations = ('+', '-', '*', '/')
    while True:
        op = input("Выберите операцию (+, -, *, /): ").strip()
        if op in valid_operations:
            return op
        print("Ошибка: неверная операция. Попробуйте еще раз.")

def display_result(num1: float, op: str, num2: float, result: float):
    """Выводит результат на экран."""
    print(f"\nРезультат: {num1} {op} {num2} = {result}")

