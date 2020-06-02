#!/usr/bin/python3
"""Inheritance"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits BaseGeometry"""


def __init__(self, width, height):
    """Instantiation with width and height"""
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height


def area(self):
    """implement the area func"""
    return self.__width * self.__height


def __str__(self):
    """prints"""
    print("[Rectangle] {}/{}".format(self.__width, self.__height))
