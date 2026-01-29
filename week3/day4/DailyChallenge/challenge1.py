import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError('Specify or the radius or the diameter of the '
                             'circle')

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"The radius of the Circle is {self.radius} and the diameter is {self.diameter}"

    def __repr__(self):
        return f"Circle(radius = {self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        else:
            raise TypeError

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


c1 = Circle(radius=5)
c2 = Circle(diameter=20)

print(f"C1: {c1}")
print(f"C2: {c2}")
print(f"c1 area: {c1.area:.2f}")

# Addition
c3 = c1 + c2
print(f"C3 (C1 + C2): {c3}")

# Comparaison
print(f"C2 is bigger than C1 ? {c2 > c1}")

# Tri d'une liste
circles = [Circle(10), Circle(1), Circle(5)]
circles.sort()
print(f"Circle sorted : {circles}")
