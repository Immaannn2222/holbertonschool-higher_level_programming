#!/usr/bin/python3
"""Python I/O"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) is not True:
            return self.__dict__
        else:
            m = {}
            for x in attrs:
                    if type(x) is not str:
                        return self.__dict__
                    if x in self.__dict__:
                        m[x] = self.__dict__[x]
            return m

    def reload_from_json(self, json):
        for v in json.keys():
            self.__dict__[v] = json[v]
