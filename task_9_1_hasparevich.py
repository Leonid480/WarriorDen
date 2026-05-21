strings = ["первая строка", "вторая строка", "третья строка"]
new_strings = [f"{i} - {string}" for i, string in enumerate(strings, start=1)]

print(new_strings)
