#!/usr/bin/python3
"""empty class BaseGeometry."""


class BaseGeometry:
    """Instance method area"""
    def area(self):
        """Raises an exception because...
        area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if self.value != type(int):
            raise TypeError("<name> must be an integer")
        if self.value == 0 or value < 0:
            raise ValueError("<name> must be greater than 0")
