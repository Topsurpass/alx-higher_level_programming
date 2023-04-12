#!/usr/bin/python3

"""
This module contains a function that writes a string to a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write string to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
