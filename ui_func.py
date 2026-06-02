from exceptions import InvalidNumberError, InvalidOperationError
from func import add, deduct, multiplication, divide

def get_numbers():
    """Получает и валидирует два числа от пользователя."""
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1, num2
    except ValueError:
        raise InvalidNumberError("Ошибка: введено не число. Пожалуйста, введите корректные значения.")

def get_operation():
    """Получает и валидирует выбор операции."""
    op = input("Выберите операцию (+, -, *, /) или 'q' для выхода: ")
    if op not in ('+', '-', '*', '/', 'q'):
        raise InvalidOperationError("Ошибка: неверная операция. Выберите +, -, *, / или q.")
    return op

def calculator_ui():
    """Запуск бесконечного цикла калькулятора."""
    print("--- Консольный Калькулятор ---")
    
    while True:
        try:
            op = get_operation()
            
            if op == 'q':
                print("Выход из программы. До свидания!")
                break
                
            num1, num2 = get_numbers()
            
            result = None
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = deduct(num1, num2)
            elif op == '*':
                result = multiplication(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
                
            print(f"Результат: {result}\n")

        except (InvalidNumberError, InvalidOperationError, ZeroDivisionError) as e:
            print(f"{e}\n")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}\n")
