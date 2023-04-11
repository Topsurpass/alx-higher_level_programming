#!/usr/bin/python3

"""
This module contains function that checks if the object
pased is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of specified
    class

    Args:
        obj: The object to check
        a_class: The specified class

    Return:
        True: If obj is exactly and instance
        False: If otherwise
    """
    return type(obj) == a_class
