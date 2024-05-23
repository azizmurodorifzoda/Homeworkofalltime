import math

class Perimeter:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius
a=int(input())
my_perimeter = Perimeter(a)
print(my_perimeter.area())
print(my_perimeter.perimeter())