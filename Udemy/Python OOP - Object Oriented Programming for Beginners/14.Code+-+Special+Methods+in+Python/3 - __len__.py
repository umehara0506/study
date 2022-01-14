"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# Example: Length of Built-in Data Types

my_string = "Hello, World!"
print(len(my_string))
print(my_string.__len__())

my_list = [1, 2, 3, 4, 5]
print(len(my_list))
print(my_list.__len__())

my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(my_tuple.__len__())

my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))
print(my_dict.__len__())


# Example: Customizing Length

class Backpack:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("This item is not in the backpack")

    def __len__(self):
        return len(self.items)


my_backpack = Backpack()

my_backpack.add_item("Water Bottle")
my_backpack.add_item("First Aid Kit")
my_backpack.add_item("Sleeping Bag")

print(len(my_backpack))

my_backpack.remove_item("Sleeping Bag")
print(len(my_backpack))

my_backpack.remove_item("Water Bottle")
my_backpack.remove_item("First Aid Kit")
print(len(my_backpack))

my_backpack.remove_item("Water Bottle")
