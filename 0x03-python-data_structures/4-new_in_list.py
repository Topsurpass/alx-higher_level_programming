#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx >= len(copy_list) or idx < 0:
        return copy_list
    copy_list[idx] = element
    return copy_list
