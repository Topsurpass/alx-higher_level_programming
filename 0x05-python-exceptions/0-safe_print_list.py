#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    length = 0
    while length < x:
        try:
            print("{}".format(my_list[length]), end="")
        except IndexError:
            break
        length += 1
    print("")
    return length
