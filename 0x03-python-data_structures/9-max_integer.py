#!/usr/bin/python3


def max_integer(my_list=[]):
    my_list.sort()
    return my_list[len(my_list) - 1] if len(my_list) > 0 else None
