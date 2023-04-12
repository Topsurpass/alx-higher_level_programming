#!/usr/bin/python3

"""
This module contains a function that returns a pascal's triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    pascal's triangle

    Args:
        n: length of the triangle
    """
    arr = [[1]]
    for row in range(n - 1):
        j = [1]
        for i in range(row):
            j.append(arr[-1][i] + arr[-1][i + 1])
        j.append(1)
        arr.append(j)
    return arr
