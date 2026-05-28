import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass

class Circle(Figure):
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Triangle(Figure):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def _get_sides(self) -> tuple[float, float, float]:
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        return a, b, c

    def perimeter(self) -> float:
        return sum(self._get_sides())

    def area(self) -> float:
        a, b, c = self._get_sides()
        p = self.perimeter() / 2
      
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Square(Figure):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def _get_side(self) -> float:
        return self.p1.distance_to(self.p2)

    def perimeter(self) -> float:
        return self._get_side() * 4

    def area(self) -> float:
        return self._get_side() ** 2
