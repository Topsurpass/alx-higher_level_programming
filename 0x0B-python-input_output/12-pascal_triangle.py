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
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri_arr = [[1]]
    for rows in range(n-1):
        tri_arr.append([a+b for a, b
                         in zip([0] + tri_arr-1], tri_arr[-1] + [0])])
    return tri_arr 
