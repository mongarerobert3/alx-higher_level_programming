#!/usr/bin/python3

from hamcrest import none
"""first class Base"""

class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):

        """Assigning attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


