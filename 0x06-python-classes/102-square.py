#!/usr/bin/python3
"""
    Module 102-square
    It defines a square by private instance attribute

"""


class Square:
    """
    This defines a square by private attribute

        Attributes:
            size: The size of the square

        Methods:
            __init__(self, size=0)
            __le__(self, other):
            __lt__(self, other):
            __gt__(self, other):
            __ge__(self, other):
            __eq__(self, other):
            __ne__(self, other):
            area(self)

    """

    def __init__(self, size=0):
        """
        This initializes the instance / object with optional
        size (integer)

        Args:
            size: The size of the square

        """
        self.size = size

    @property
    def size(self):
        """
        getter method
        Returns:
            size

        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        setter method

        Args:
            new_size: The new size

        Raises:
            TypeError: if size is not an integer or float
            ValueError: if size is less than 0 i.e negavive

        """
        if type(new_size) != int:
            raise TypeError("size must be a number")

        elif new_size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = new_size

    def area(self):
        """
        Computes the area of the square by raising size to power of 2

        Returns:
            The area of the square

         """
        return self.__size**2

    def __eq__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if both objects are equal
            False: if otherwise

        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if both objects not equal
            False: if otherwise

        """
        return self.size != other.size

    def __gt__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if first object is greater than the other
            False: if otherwise

        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if first object is greater than or equal the other
            False: if otherwise

        """
        return self.size >= other.size

    def __lt__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if first object is less that the other
            False: if otherwise

        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compare 2 instances / objects of a class

        Args:
            other: the other object

        Return:
            True: if first object is less than or equal the other
            False: if otherwise

        """
        return self.size <= other.size
