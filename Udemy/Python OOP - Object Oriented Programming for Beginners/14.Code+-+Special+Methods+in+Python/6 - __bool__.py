"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

# Example before defining the __bool__() method.

class BankAccount:

    def __init__(self, account_owner, account_number, initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = initial_balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds.")

my_account = BankAccount("Nora Nav", "356-2456-2455", 45045.23)
print(bool(my_account))

if my_account:
    print("True")
else:
    print("False")

my_account.balance = 0
print(bool(my_account))

if my_account:
    print("True")
else:
    print("False")


# Example after defining the __bool__() method.

class BankAccount:

    def __init__(self, account_owner, account_number, initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = initial_balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def __bool__(self):
        return self.balance > 0

my_account = BankAccount("Nora Nav", "356-2456-2455", 45045.23)
print(bool(my_account))

if my_account:
    print("True")
else:
    print("False")

my_account.balance = 0
print(bool(my_account))
print(my_account.balance)

if my_account:
    print("True")
else:
    print("False")


# Examples of where the length determines the boolean value.

# List
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

if my_list:
    print("The list is not empty.")
    print(bool(my_list))
else:
    print("The list is empty.")
    print(bool(my_list))

# String
my_string = "Hello, World!"
print(len(my_string))

if my_string:
    print("The string is not empty.")
    print(bool(my_string))
else:
    print("The string is empty.")
    print(bool(my_string))
