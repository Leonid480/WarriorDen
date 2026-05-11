# Исходный список
original_list = [1, -4, 10, 9, 3]

# Создание нового списка (элемент * -2)
new_list = [x * -2 for x in original_list]

print(f"Исходный список: {original_list}")
print(f"Новый список: {new_list}")

#Через цикл while
# Исходный список
original_list = [1, -5, 10, -2, 3]

# Создаем пустой список для результатов
new_list = []

# Индекс для цикла while
i = 0

# Цикл while для перебора элементов
while i < len(original_list):
    # Умножаем элемент на -2 и добавляем в новый список
    new_list.append(original_list[i] * -2)
    # Увеличиваем индекс
    i += 1

# Вывод результатов
print("Исходный список:", original_list)
print("Новый список:", new_list)