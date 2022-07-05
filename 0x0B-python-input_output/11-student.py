#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """student directory"""
        class_d = self.__dict__
        self_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    self_d[attr] = class_d[attr]

            return self_d
        return class_d

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
