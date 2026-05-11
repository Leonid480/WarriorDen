original_list = [1, 2, 3, 4, 5]
new_list = []

# Переносим элементы начиная со второго на новые позиции
for i in range(1, len(original_list)):
    new_list.append(original_list[i])

# Переносим первый элемент в конец
new_list.append(original_list[0])

print(new_list)  

#через while
original_list = [1, 2, 3, 4, 5]
new_list = []
length = len(original_list)

# Если список пуст или с одним элементом, сдвиг не нужен
if length > 1:
    i = 1
    
    while i < length:
        new_list.append(original_list[i])
        i += 1
    
   
    new_list.append(original_list[0])
else:
    new_list = original_list.copy()

print(f"Исходный: {original_list}")
print(f"Сдвинутый: {new_list}")