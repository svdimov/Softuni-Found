class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.pi * self.radius * self.radius # **2
        return area

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
