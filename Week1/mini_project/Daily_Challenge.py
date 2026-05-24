# Daily Challenge : Circle Class

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        # Accept either radius or diameter
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = 0

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    # Dunder method : print circle info
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"

    # Dunder method : add two circles
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # Dunder method : compare which is bigger
    def __gt__(self, other):
        return self.radius > other.radius

    # Dunder method : check if equal
    def __eq__(self, other):
        return self.radius == other.radius

    # Dunder method : needed for sorting
    def __lt__(self, other):
        return self.radius < other.radius


# Test
c1 = Circle(radius=5)
c2 = Circle(radius=3)
c3 = Circle(diameter=12)  # radius = 6
c4 = Circle(radius=1)

# Print circle info
print(c1)
print(c2)
print(c3)

# Area
print(f"Area of c1: {c1.area()}")

# Add two circles
c5 = c1 + c2
print(f"c1 + c2 = {c5}")

# Compare circles
print(f"c1 > c2 ? {c1 > c2}")
print(f"c1 == c2 ? {c1 == c2}")

# Sort circles
circles = [c1, c2, c3, c4]
sorted_circles = sorted(circles)
print("\nSorted circles:")
for c in sorted_circles:
    print(c)