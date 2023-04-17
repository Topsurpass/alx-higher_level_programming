#!/usr/bin/python3

"""
This module contains a class that inherits from the base class 'Base'
"""
from models.base import Base


class Rectangle(Base):
    """This class creates a rectangle. It inherits from
    the Baseclass Base.

    Attributes:
        Fields:
            __width: The width of the rectangle
            __height: The height of the rectangle
            __x
            __y
        Methods:
            __init__(self, width, height, x=0, y=0, id=None):
                Initializes object
            __str__(self): Print objects in string
            super().__init__(id): Initialize Base class attribute
            area(self): The area of the rectangle
            width(self, value): Width setter
            height(self, value): Height setter
            x(self): x getter
            x(self, value): x setter
            y(self): y getter
            y(self, value): y setter
            display(self): Print to stdout
            update(self, *args, **kwargs): Update attributes
            to__dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Return x"""
        return self.__x

    @property
    def y(self):
        """Return y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set new value for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set new value for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set new value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set new value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle to stdout"""
        print("\n" * self.__y + "\n".join(
            " " * self.__x + "#" * self.__width for i in range(self.__height)))

    def __str__(self):
        """print the object as a string"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign an argument to each object attribute"""
        if args and len(args) != 0:
            for i, args in enumerate(args):
                if i == 0:
                    self.id = args
                elif i == 1:
                    self.__width = args
                elif i == 2:
                    self.__height = args
                elif i == 3:
                    self.__x = args
                elif i == 4:
                    self.__y = args
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """Return dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
