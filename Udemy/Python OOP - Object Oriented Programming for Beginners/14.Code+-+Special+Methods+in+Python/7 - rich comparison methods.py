"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# Examples of Comparison Operators and Built-in Data Types

print(15 <= 8)
print(4 > 4)
print(5 == 5)
print(6 != 8)

print("Hello" < "World")
print("Python" >= "Java")
print("Hello" == "Hello")

print([1, 2, 3, 4] < [1, 2, 3, 5])
print([4, 5, 6] > [1, 2, 3, 4])


# Example: Comparing instances of the Circle Class

class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return (self.radius <= other.radius
                and self.color == other.color)

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return (self.radius >= other.radius
                and self.color == other.color)

    def __eq__(self, other):
        return (self.radius == other.radius
                and self.color == self.color)

    def __ne__(self, other):
        return (self.radius != other.radius
                or self.radius != other.radius)

circleA = Circle(5, "Blue")
circleB = Circle(5, "Green")
circleC = Circle(7, "Red")
circleD = Circle(5, "Blue")

print(circleA < circleB)
print(circleA <= circleB)

print(circleA > circleD)
print(circleA >= circleD)

print(circleA == circleB)
print(circleA == circleD)
print(circleA != circleD)
