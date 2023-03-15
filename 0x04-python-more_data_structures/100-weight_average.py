#!/usr/bin/python3


def weight_average(my_list=[]):
    product = 0
    avg = 0

    for i in my_list:
        calc = i[0] * i[1]
        product += calc
        avg += i[1]
    return product / avg
