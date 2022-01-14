"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

def print_floyds_triangle(n):
    """Print Floyd's Triangle with n rows."""
    count = 1

    for i in range(1, n+1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()
