import sys
from classes import Math
from ui_func import get_number, get_operation, display_result
from exceptions import CalculationError

def main():
    print("Консольный калькулятор (версия 2026)")
    
    try:
        # Ввод данных
        num1 = get_number("Введите первое число: ")
        operation = get_operation()
        num2 = get_number("Введите второе число: ")
        
        # Создание объекта и вычисления
        math_obj = Math(num1, num2)
        
        if operation == '+':
            result = math_obj.add()
        elif operation == '-':
            result = math_obj.subtract()
        elif operation == '*':
            result = math_obj.multiply()
        elif operation == '/':
            result = math_obj.divide()
            
        # Вывод
        display_result(num1, operation, num2, result)
        
    except CalculationError as e:
        print(f"\n[Ошибка]: {e}")
    except Exception as e:
        print(f"\n[Непредвиденная ошибка]: {e}")

if __name__ == "__main__":
    main()
