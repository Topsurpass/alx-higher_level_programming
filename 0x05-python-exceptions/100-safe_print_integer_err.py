#!/usr/bin/python3


from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
    except (ValueError, TypeError) as exc:
        stderr.write("Exception:{}\n".format(exc))
        return False
    return True
