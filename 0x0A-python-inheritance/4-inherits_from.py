#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """logic
        Args:  obj(any): object of the class
        a_class(type): describes the class
    """
    while type(obj) != a_class:
        return isinstance(obj, a_class)
