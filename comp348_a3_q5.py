import itertools
import math
from typing import Final


class Shape(object):
    id_iter = itertools.count()

    def __init__(self):
        # PEP 591: Final for Linters/Type Checkers https://peps.python.org/pep-0591/
        # https://stackoverflow.com/questions/50533812/what-is-the-best-way-to-define-constant-variables-python-3/65706030#65706030
        self.ID: Final[int] = next(Shape.id_iter)+1

    def __str__(self):
        return str(self.ID) + ": " + self.__class__.__name__ + ", perimeter: " + str(self.perimeter()) \
               + ", area: " + str(self.area())

    def perimeter(self):
        return "undefined"

    def area(self):
        return "undefined"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius if self.radius >= 0 else "undefined"

    def area(self):
        return math.pi * self.radius**2 if self.radius >= 0 else "undefined"


class Ellipse(Shape):
    def __init__(self, first, second):
        super().__init__()
        self.a = first if first >= second else second
        self.b = first if first < second else second

    def area(self):
        return math.pi * self.a * self.b if (self.a >= 0 and self.b >= 0) else "undefined"

    def eccentricity(self):
        try:
            c = math.sqrt(self.a**2 - self.b**2)
        except ValueError:
            return "undefined"
        return c if (self.a >= 0 and self.b >= 0) else "undefined"


class Rhombus(Shape):
    def __init__(self, p, q):
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        return 2 * math.sqrt(self.p**2 + self.q**2) if (self.p >= 0 and self.q >= 0) else "undefined"

    def area(self):
        return self.p * self.q / 2 if (self.p >= 0 and self.q >= 0) else "undefined"

    def inradius(self):
        try:
            r = self.p * self.q / self.perimeter()
        except ValueError:
            return "undefined"
        except TypeError:
            return "undefined"
        return r if r >= 0 else "undefined"


if __name__ == '__main__':
    shapes = [Shape() for i in range(10)]
    print("(1b) ID:", end=' ')
    for shape in shapes:
        print(shape.ID, end=' ')
    print()
    print(shapes[0].ID, end=' ')
    shapes[0].ID = 15  # Should show warning for many Linters/Type Checkers
    print(shapes[0].ID)
    print()

    print("(1c): " + str(shapes[0]))
    print()

    circle = Circle(4)
    print(circle)
    print()

    ellipse = Ellipse(4, 2)
    print(ellipse)
    print("(3d) linear eccentricity: " + str(ellipse.eccentricity()))
    ellipse.a = 1
    print(ellipse)
    print("(3d) linear eccentricity: " + str(ellipse.eccentricity()))
    print()

    rhombus = Rhombus(4, 2)
    print(rhombus)
    print("(4d) in-radius: " + str(rhombus.inradius()))
    rhombus.p = -1
    print(rhombus)
    print("(4d) in-radius: " + str(rhombus.inradius()))
