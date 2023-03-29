#!/usr/bin/python3

"""Interpretation of MagicClass bytescode to it's actual class definition"""
import math


class MagicClass:
    """
    MagicClass from bytecode

    Attributes:
        radius: the radius of the circle to be supplied

    Methods:
        __init__(self, radius=0)
        area(self)
        circumference(self)

    """
    def __init__(self, radius=0):
        """
        Initializes class instance or object

        Args:
            radius: The radius of circle

        Raises:
            TypeError: if radius is not an integer or float

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Clculate area

        Returns:
            area of a circle: 2 * pi * square of radius

        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate circumference

        Returns:
            circumference of a circle: 2 * pi * radius

        """
        return (2 * math.pi * self.__radius)
