#!/usr/bin/python3

"""Function to add the integers"""
def add_integer(a, b=98):
    """Adding the integers
    Args:
        a - first number input
        b- seond number input
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
