#!/usr/bin/python3
"""Python classes"""


class Square():
    """Print square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """square area"""
        return self.__size ** 2

    @property
    def size(self):
        """square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints the square"""
        for count1 in range(self.__size):
            for count2 in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
