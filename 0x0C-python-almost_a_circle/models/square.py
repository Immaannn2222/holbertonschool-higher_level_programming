#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """display"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
