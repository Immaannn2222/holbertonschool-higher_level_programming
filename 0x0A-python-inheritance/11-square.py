#!/usr/bin/python3
"""Inheritance"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """"Instantiation of size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)


    def __str__(self):
        """prints"""
        return("[Square] {}/{}".format(self.__size, self.__size))
