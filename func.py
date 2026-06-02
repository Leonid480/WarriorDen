def add(a, b):
    return a + b

def deduct(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b
