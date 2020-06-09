#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter of width"""
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__width = width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of height"""
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = height

    @property
    def x(self):
        """gettter of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter of x"""
        if x < 0:
            raise ValueError("x must be >= 0")
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        else:
            self.__x = x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter of y"""
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculate the area"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle in #"""
        for l in range(self.__y):
            print("")
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """updayte"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            if i == 1:
                self.width = j
            if i == 2:
                self.height = j
            if i == 3:
                self.x = j
            if i == 4:
                self.y = j

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "width":
                self.width = v
            if k == "height":
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = {'x': self.x, 'y': self.y, 'id': self.id,
                     'height': self.height, 'width': self.width}
        return rect_dict
