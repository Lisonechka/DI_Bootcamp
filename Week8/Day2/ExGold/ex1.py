# Exercise 1 : Geometry
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

    def definition(self):
        print(f'Circle with area {self.area()} and perimeter {self.perimeter()}')


circle1 = Circle(3)
print(circle1.area())
print(circle1.perimeter())
circle1.definition()

