#!/usr/bin/python3
"""
    Module 1-square
    It defines a square by private instance attribute

"""


class Square:
    """This defines a square by private attribute

        Attributes:
            size: The size of the square

    """

    def __init__(self, size):
        """
        This initializes the instance / object with
        size (no type / value verification)

        Args:
            size: The size of the square

        """
        self.__size = size
