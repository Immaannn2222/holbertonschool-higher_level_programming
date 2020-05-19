#!/usr/bin/python3
"""Python classes"""


class Square:
    """acc and update p.attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if isinstance(value, int) is False:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise Exception
        except ValueError:
            print("size must be >= 0", end="")
            raise Exception
        self.__size = value

    def area(self):
        return self.__size * self.__size
