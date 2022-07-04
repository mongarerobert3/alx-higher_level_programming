#!/usr/bin/python3
"""True if the object is exactly an instance of the specified class ;
otherwise False."""


def is_same_class(obj, a_class):
    """logic
        Args:
        obj - object of the class
        a_class - the class
    """
    if type(obj) == a_class:
        return True
    return False
