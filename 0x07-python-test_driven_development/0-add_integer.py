#!/usr/bin/python3
"""

Task 0 - Integers addition

"""

def add_integer(a, b=98):
    """
    Function that adds 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
