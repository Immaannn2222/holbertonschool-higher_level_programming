#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle proporties"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__height <= 0 or self.__width <= 0:
            return ""
        new_str = ""
        for x in range(self.__height):
            new_str += "#" * self.__width
            new_str += '\n'
        return new_str[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
