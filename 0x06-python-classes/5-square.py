#!/usr/bin/python3
"""2-square.py"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Getter and setter for private size variable"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Finds the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the area"""
        for i in range(self.__size):
            print("#" * self.size)
        if self.size == 0:
            print()
