#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """display"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
    super(Square, type(self)).width.fset(self, size)

    def update(self, *args, **kwargs):
        """update"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            if i == 1:
                self.width = j
                self.height = j
            if i == 2:
                self.x = j
            if i == 3:
                self.y = j

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "size":
                self.width = v
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        rect_dict = {'x': self.x, 'y': self.y, 'id': self.id,
                     'size': self.width}
        return rect_dict
