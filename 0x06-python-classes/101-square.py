#!/usr/bin/python3
"""
    Module 5-square
    It defines a square by private instance attribute

"""


class Square:
    """This defines a square by private attribute

        Attributes:
            size: The size of the square
            position: Tuple of 2 positive integers

        Methods:
            __init__(self, size=0)
            area(self)
            my_print(self)

    """

    def __init__(self, size=0, position=(0, 0)):
        """This initializes the instance / object with optional
        size (integer)

        Args:
            size: The size of the square
            position: Tuple of 2 positive integers

        """
        self.size = size
        self.position = position

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
            TypeError: if size is not an integer
            ValueError: if size is less than 0 i.e negavive

        """
        if type(new_size) != int:
            raise TypeError("size must be an integer")

        elif new_size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = new_size

    @property
    def position(self):
        """
        getter method

        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, nw_positn):
        """
        setter method

        Args:
            nw_positn: The new position turple

        Raises:
            TypeError: If the turple is not of 2 integers

        """
        if len(nw_positn) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in nw_positn:
                if type(i) != int or i < 0:
                    raise TypeError("position must be a tuple of 2\
                            positive integers")
                    break
            self.__position = nw_positn

    def area(self):
        """Computes the area of the square by raising size to power of 2

        Returns:
            The area of the square

         """
        return (self.__size**2)

    def my_print(self):
        """Print to stdout the square with character # and with spaces"""

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([
                " " * self.__position[0] + "#" * self.__size
                for rows in range(self.__size)
                ]))

    def __str__(self):
        """
        String representation of object / instance of the class

        Example: print(my_square) which is an instance of the class defined
        """

        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([
            " " * self.__position[0] + "#" * self.__size
            for rows in range(self.__size)
            ])

        return string
