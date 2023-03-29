#!/usr/bin/python3

"""
    Module 100-singly_linked_list
    A class Node that defines a node of a singly linked list
    A class that defines a singly linked list
"""


class Node:
    """This class defines a node of a singly linked list

    Methods:
        __init__(self, data, next_node=None)

    Attributes:
        data: The node data
        next_node: pointer to the next node

    """
    def __init__(self, data, next_node=None):
        """Initialize the object / instance of the class

        Args:
            data: The node's data
            next_node: Pointer address to the next node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter method

        Return: the new data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter method

        Set the new value for the node's data

        Raises:
            TypeError: if data is not an integer

        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter method

        Return: the pointer to the next node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter method

        Set the new value for the next node

        Raises:
            TypeError: if next_node is not equal to either Node or None

        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list

    Attributes:
        head: Private

    Methods:
        __init__(self)
        sorted_insert(self, value)

    """
    def __init__(self):
        """
        Initializes the object / instance of the class

        Attributes:
            head: Private

        """
        self.__head = None

    def __str__(self):
        """
        String representation of of singly linked list
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts new nodes into the singly linked list in a sorted order

        Args:
            value: the integer data for node

        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        temp = self.__head
        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while temp.next_node is not None and new.data > temp.next_node.data:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
