#!/usr/bin/python3
"""Python classes"""


class Square():
    """definition of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
                raise TypeError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if not isinstance(value, tuple) or len(value) != 2\
           or not isinstance(value[0], int)\
           or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(' ', end='')
                for y in range(self.__size):
                    print('#', end='')
                print()
