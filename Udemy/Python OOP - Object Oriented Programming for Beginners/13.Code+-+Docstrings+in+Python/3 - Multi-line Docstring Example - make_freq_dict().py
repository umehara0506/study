"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

def make_frequency_dict(sequence):
    """Return a dictionary that maps each element in sequence to its frequency.

    Create a dictionary that maps each element in the list sequence
    to the number of times the element occurs in the list. The element
    will be the key of the key-value pair in the dictionary and its frequency
    will be the value of the key-value pair.

    Argument:
        sequence: A list of values. These values have to be of an
            immutable data type because they will be assigned as the keys
            of the dictionary. For example, they can be integers, booleans,
            tuples, or strings.

    Return:
        A dictionary that maps each element in the list to its frequency.
        For example, this function call:

        make_frequency_dict([1, 6, 2, 6, 2])

        returns this dictionary:

        {1: 1, 6: 2, 2: 2}

    Raise:
        ValueError: if the list is empty.
    """
    if not sequence:
        raise ValueError("The list cannot be empty")

    freq = {}

    for elem in sequence:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1

    return freq
