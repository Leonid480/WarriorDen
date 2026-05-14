# 12 функций для перевода величин
def inches_to_cm(inches): return inches * 2.54
def cm_to_inches(cm): return cm / 2.54
def miles_to_km(miles): return miles * 1.60934
def km_to_miles(km): return km / 1.60934
def pounds_to_kg(pounds): return pounds * 0.453592
def kg_to_pounds(kg): return kg / 0.453592
def ounces_to_grams(ounces): return ounces * 28.3495
def grams_to_ounces(grams): return grams / 28.3495
def gallons_to_liters(gallons): return gallons * 3.78541
def liters_to_gallons(liters): return liters / 3.78541
def pints_to_liters(pints): return pints * 0.473176
def liters_to_pints(liters): return liters / 0.473176

def show_menu():
    print("\n" + "="*30)
    print("КОНВЕРТЕР ВЕЛИЧИН")
    print("="*30)
    print("1.  Дюймы в сантиметры")
    print("2.  Сантиметры в дюймы")
    print("3.  Мили в километры")
    print("4.  Километры в мили")
    print("5.  Фунты в килограммы")
    print("6.  Килограммы в фунты")
    print("7.  Унции в граммы")
    print("8.  Граммы в унции")
    print("9.  Галлоны в литры")
    print("10. Литры в галлоны")
    print("11. Пинты в литры")
    print("12. Литры в пинты")
    print("0.  Выход")
    print("="*30)

def main():
    while True:
        show_menu()
        choice = input("Выберите вариант (0-12): ")

        if choice == '0':
            print("Выход из программы. До свидания!")
            break
        
        # Словарь функций для удобного вызова по номеру
        functions = {
            '1': ('дюймы', 'см', inches_to_cm),
            '2': ('см', 'дюймы', cm_to_inches),
            '3': ('мили', 'км', miles_to_km),
            '4': ('км', 'мили', km_to_miles),
            '5': ('фунты', 'кг', pounds_to_kg),
            '6': ('кг', 'фунты', kg_to_pounds),
            '7': ('унции', 'граммы', ounces_to_grams),
            '8': ('граммы', 'унции', grams_to_ounces),
            '9': ('галлоны', 'литры', gallons_to_liters),
            '10': ('литры', 'галлоны', liters_to_gallons),
            '11': ('пинты', 'литры', pints_to_liters),
            '12': ('литры', 'пинты', liters_to_pints)
        }

        if choice in functions:
            unit_from, unit_to, func = functions[choice]
            try:
                value = float(input(f"Введите значение ({unit_from}): "))
                result = func(value)
                print(f"--- Результат: {value} {unit_from} = {result:.4f} {unit_to} ---")
            except ValueError:
                print("Ошибка: Введите численное значение!")
        else:
            print("Неверный ввод. Пожалуйста, выберите от 0 до 12.")

main()
