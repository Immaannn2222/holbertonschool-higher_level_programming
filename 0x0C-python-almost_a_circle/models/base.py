#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or (len(list_dictionaries) == 0):
            return"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        li = []
        filname = cls.__name__+".json"
        for j in list_objs:
            li.append(cls.to_dictionary(j))
        with open(filname, "w") as fi:
            fi.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_srting):
        """returns the JSON string representation"""
        if json_srting is None or json_srting = "":
            return"[]"
        else:
            return json.loads(json_srting)
