#!/usr/bin/python3

"""
This module contains a class that inherits from class int
and inverts its equality and non equality operation
"""


class MyInt(int):
    """This derived class of the base class int

    Attributes:
        __init__(self, numb)
        __eq__(self, value)
        __ne__(self, value)
        num: The number to be supplied
    """

    def __init__(self, numb):
        """Initialize the object
        Args:
            num: Value to be supplied
        """
        self.num = numb

    def __eq__(self, value):
        """Return the inverted result of the equality operation
        of int
        """
        return (self.num != value)

    def __ne__(self, value):
        """Return the inverted result of the non-equality operation
        of the int
        """
        return (self.num == value)
