data = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

# Создаем новый словарь, используя метод .keys() для доступа к ключам
new_data = {}
for key in data.keys():
    new_key = f"{key}{len(key)}" # Создаем новый ключ: имя + длина
    new_data[new_key] = data[key]

print(new_data)
# через while
data = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_data = {}

# Получаем список ключей
keys = list(data.keys())
i = 0

# Используем метод while
while i < len(keys):
    old_key = keys[i]
    # Создаем новый ключ: имя + длина имени
    new_key = f"{old_key}{len(old_key)}"
    new_data[new_key] = data[old_key]
    i += 1