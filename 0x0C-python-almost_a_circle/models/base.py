#!/usr/bin/python3
"""Base module"""
import json
import turtle


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
        if list_objs is not None:
            for j in list_objs:
                li.append(cls.to_dictionary(j))
        with open(filname, "w") as fi:
            fi.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_srting):
        """returns the JSON string representation"""
        if not json_srting or json_srting == "":
            json_srting = "[]"
        return json.loads(json_srting)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(6, 19)
        if cls.__name__ == 'Square':
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        li = []
        filname = cls.__name__+".json"
        with open(filname, "r+") as fi:
            j = cls.from_json_string(fi.read())
        if j is not None:
            for i in j:
                li.append(cls.create(**i))
        return li

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        t = turtle.Turtle()
        t.color("green")
        t.shape("turtle")
