from classes import Point, Circle, Triangle, Square

figures = [
    Circle(center=Point(0, 0), radius=5),
    Triangle(p1=Point(0, 0), p2=Point(3, 0), p3=Point(0, 4)),
    Square(p1=Point(0, 0), p2=Point(4, 4))
]

for i, figure in enumerate(figures, 1):
    figure_name = type(figure).__name__
    print(f"Площадь фигуры {i} ({figure_name}): {figure.area():.2f}")
