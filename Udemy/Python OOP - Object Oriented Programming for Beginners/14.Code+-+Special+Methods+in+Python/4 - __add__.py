"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# Examples with Built-in Functions

print(3 + 4)
print((3).__add__(4))

print("Hello " + "World!")
print("Hello ".__add__("World!"))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3].__add__([4, 5, 6]))


# Example with User-Defined Class

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"


pointA = Point2D(5, 6)
print(pointA)

pointB = Point2D(2, 3)
print(pointB)

pointC = pointA + pointB
print(pointC) 
