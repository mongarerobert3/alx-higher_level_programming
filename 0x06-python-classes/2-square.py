#!/usr/bin/python3

"""
    square
"""


from multiprocessing.sharedctypes import Value


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Private instance attribute
            Args:
                size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
