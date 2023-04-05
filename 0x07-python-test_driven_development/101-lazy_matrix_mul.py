#!/usr/bin/python3

"""
Module 101-lazy_matrix-mul
Ths module contains functions that multiply 2 matrices together
using the numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return matrix multiplied together using numpy"""
    return np.dot(m_a, m_b)
