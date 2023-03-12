#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    l1 = len(tuple_a)
    l2 = len(tuple_b)
    a_val_1 = tuple_a[0] if l1 > 0 else 0
    a_val_2 = tuple_a[1] if l1 > 1 else 0
    b_val_1 = tuple_b[0] if l2 > 0 else 0
    b_val_2 = tuple_b[1] if l2 > 1 else 0

    return ("{}".format((a_val_1 + b_val_1, a_val_2 + b_val_2)))
