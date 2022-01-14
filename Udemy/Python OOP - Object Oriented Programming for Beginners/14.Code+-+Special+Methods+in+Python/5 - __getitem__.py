"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# Examples with List Data Type

my_list = ["a", "b", "c", "d"]

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print("-----")

print(my_list.__getitem__(0))
print(my_list.__getitem__(1))
print(my_list.__getitem__(2))
print(my_list.__getitem__(3))


# Example with User-Defined Class

class Bookshelf:

    def __init__(self):
        self.content = [[],
                        [],
                        []]

    def add_book(self, book, location):
        self.content[location].append(book)

    def take_book(self, book, location):
        self.content[location].remove(book)

    def __getitem__(self, location):
        return self.content[location] 


my_bookshelf = Bookshelf()

my_bookshelf.add_book("Les Miserables", 0)
my_bookshelf.add_book("Pride and Prejudice", 0)
my_bookshelf.add_book("Frankenstein", 0)

my_bookshelf.add_book("Sense and Sensibility", 1)
my_bookshelf.add_book("Jane Eyre", 1)
my_bookshelf.add_book("The Little Prince", 1)

my_bookshelf.add_book("Moby Dick", 2)
my_bookshelf.add_book("The Adventures of Huckleberry Finn", 2)
my_bookshelf.add_book("Dracula", 2)

print(my_bookshelf[0])
print(my_bookshelf[1])
print(my_bookshelf[2])
