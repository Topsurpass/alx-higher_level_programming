#!/usr/bin/python3

"""
Module 101-locked_class
This module contains a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance.
"""


class LockedClass():
    """Lock instance creation if instance attribute is not equal "first_name"
    """
    __slots__ = "first_name"
