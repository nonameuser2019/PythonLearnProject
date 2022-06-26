class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.PI * self.radius ** 2

    def get_perimetr(self):
        return 2 * Circle.PI * self.radius


if __name__ == '__main__':
    c1 = Circle(10)
    print(c1.get_area())
    print(c1.get_perimetr())