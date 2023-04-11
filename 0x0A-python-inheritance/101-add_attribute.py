#!/usr/bin/python3

"""
This module contains a function that adds a new attribute
to an object if it's possible.
"""


def add_attribute(obj, attr, value):
    """Adds attribute to an object if possible

    Args:
        obj: The object to which new attribute is
        to be added
        attr: Attribute to be added
        value: The corresponding attribute value

    Raise:
        TypeError
    """

    if ('__dict__' in dir(obj)):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add mew attribute")
