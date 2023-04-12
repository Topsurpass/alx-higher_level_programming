#!/usr/bin/python3

"""
This module contains functions that reads a text file and prints
it to stdout
"""


def read_file(filename=""):
    """Open name file and prints its contents to stdout

    Args:
        filename: The filename to read from

    Return: Nothing
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
