"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:
	"""A that represents a Backpack. 

	Attribute:
		items (list): the list of items in the backpack (initially empty).

	Methods:
		add_item(self, item):
			Add the item to the backpack.
		remove_item(self, item):
			Remove the item from the backpack.
		has_item(self, item):
			Return True if the item is in the backpack. Else, return False.
	"""
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print("This item is not in the backpack")

	def has_item(self, item):
		return item in self.items
