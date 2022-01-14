"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Polygon:
    
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle(Polygon):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height


my_triangle = Triangle(3, "Blue")

# Now the instance doesn't have these attributes.
print(my_triangle.num_sides) 
print(my_triangle.color)
