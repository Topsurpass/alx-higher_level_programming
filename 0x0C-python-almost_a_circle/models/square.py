#!/usr/bin/python3

"""
This module contains a class that inherits from another class
Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits all the methods and attributes
    of the class Rectangle to make a square

    Attributes:
        Fields:
            size: The size of the square
            x
            y

        Methods:
            __init__(self, size, x=0, y=0, id=None)
            super().__init__(size, size, x, y, id)
            __str__(self)
            size(self): The size getter
            size(self, value): The size setter
            update(self, *args, **kwargs)
            to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

        self.size = size

    @property
    def size(self):
        """Return the sizes of the square based on class
        Rectangle
        """
        return self.height

    @size.setter
    def size(self, value):
        """Set new value for the square based on
        Rectangle class
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Print instance in string"""
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attribute values"""
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Return dictionary representation of square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
