#!/usr/bin/python3


def no_c(my_string):
    copy_str = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            copy_str += ""
        else:
            copy_str += i
    return copy_str
