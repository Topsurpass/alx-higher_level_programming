#!/usr/bin/python3

"""
This module contains function that appends a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append additional text to file

    Args:
        filename: The file to append text to
        text: The text to append to file

    Return: Number of characters
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
