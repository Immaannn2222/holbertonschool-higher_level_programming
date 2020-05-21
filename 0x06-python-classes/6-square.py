#!/usr/bin/python3
"""Python classes"""


class Square():
    """definition of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
        for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if y < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        if self.__size == 0:
            print()

    @property
    def position(self):
        """square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
