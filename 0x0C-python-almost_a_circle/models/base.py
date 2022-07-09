#!/usr/bin/python3

from encodings import utf_8
from fileinput import filename
from os import path
import json
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, "w", encoding="utf_8") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())
            
            return f.write(cls.to_json_string(json_attrs))
            
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Square":
            dummy = cls(3)
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, "r", encoding="utf_8") as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
