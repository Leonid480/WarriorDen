import math

def Sin1(x, eps):
    
    total_sum = 0
    current_term = x 
    n = 1
    
    while abs(current_term) > eps:
        total_sum += current_term
        current_term *= -x**2 / ((2 * n) * (2 * n + 1))
        n += 1
        
    return total_sum


x_val = float(input("Введите значение x: "))
if x_val !=(int) or (float):
    print ("Вы ввели не число или не целое число")
eps_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

print(f"\n Вычисление sin({x_val}):")
print("-" * 40)
for eps in eps_values:
    result = Sin1(x_val, eps)
    print(f"При ε = {eps:<10} | sin ≈ {result:.8f}")

print("-" * 40)
print(f"Точное значение:     {math.sin(x_val):.8f}")
