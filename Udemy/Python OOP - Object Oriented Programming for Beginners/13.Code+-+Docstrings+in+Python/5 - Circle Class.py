"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

import math


class Circle:
    """A class that represents a circle.

    Attributes:
        radius (float): the distance from the center of the circle
            to its circumference.
        color (string): the color of the circle.
        diameter (float): the distance through the center of the circle
            from one side to the other.

    Methods:
        find_area(self):
            Return the area of the circle.
        find_perimeter(self):
            Return the perimeter of the circle.
    """

    def __init__(self, radius, color):
        """Initialize an instance of Circle.

        Arguments:
            radius (float): the distance from the center
                of the circle to its circumference.
            color (string): the color of the circle.
        """
        self._radius = radius
        self._color = color

    @property
    def radius(self):
        """Return the radius of the circle.

        This is a float that represents the distance from
        the center of the circle to its circumference."""
        return self._radius

    @property
    def color(self):
        """Return the color of the circle.

        The color is described by a string that must be capitalized.
        For example: "Red", "Blue", "Green", "Yellow".
        """
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def diameter(self):
        """Return the diameter of the circle.

        This is a float that represents the distance through
        the center of the circle from one side to the other.
        """
        return 2 * self._radius

    def find_area(self):
        """Find and return the area of a circle.

        The area is calculated with the circle radius
        using the formula Pi * (radius ** 2).
        """
        return math.pi * (self._radius ** 2)

    def find_perimeter(self):
        """Find and return the perimeter of a circle.

        The perimeter is calculated with the circle radius
        using the formula (2 * Pi * radius).
        """
        return 2 * math.pi * self._radius


help(Circle)

print(Circle.__doc__)
