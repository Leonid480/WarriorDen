class Car:

    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    def speed_up(self):
        print("""Увеличение скорости на 5.""")
        self.__speed += 5

    def speed_down(self):
        print ("""Уменьшение скорости на 5 (не меньше 0).""")
        self.__speed = max(0, self.__speed - 5)

    def stop(self):
        print("""Сброс скорости на 0.""")
        self.__speed = 0

    def display_speed(self):
        """Отображение текущей скорости."""
        print(f"Текущая скорость: {self.__speed} км/ч")

    def reverse(self):
        print("""Разворот (изменение знака скорости).""")
        self.__speed = -self.__speed

    def get_speed(self):
        return self.__speed
