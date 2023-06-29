#!/usr/bin/python3
"""
This module contains function that finds the peak in a list of unsorted
list of integers.
"""


def find_peak(list_of_integers):
    """Return number that is > the numbers both at its left and right side"""

    if not list_of_integers:
        return None

    new_list = list_of_integers[:]
    start, end = 0, len(new_list) - 1

    if new_list[start] > new_list[start+1]:
        return new_list[start]
    if new_list[end] > new_list[end-1]:
        return new_list[end]

    mid = (start+end)//2
    if new_list[mid-1] < new_list[mid] and new_list[mid+1] < new_list[mid]:
        return new_list[mid]
    if new_list[mid] < new_list[mid-1]:
        return find_peak(new_list[start:mid+1])
    elif new_list[mid] < new_list[mid+1]:
        return find_peak(new_list[mid:end+1])
    else:
        return new_list[start]
