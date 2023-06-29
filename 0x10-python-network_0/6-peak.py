#!/usr/bin/python3
"""
This module contains function that finds the peak in a list of unsorted
list of integers.
"""


def find_peak(list_of_integers):
    """Return number that is > the numbers both at its left and right side"""
    
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1
    new_list = list_of_integers[:]

    while low < high:
        mid = (low + high) // 2

        if new_list[mid] < new_list[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return new_list[low]
