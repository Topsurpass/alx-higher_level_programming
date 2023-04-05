#!/usr/bin/python3

"""
Module 101-lazy_matrix-mul
Ths module contains functions that multiply 2 matrices together
using the numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return matrix multiplied together using numpy
    Args:
        m_a: matrix a
        m_b: matrix b

    Return: Product of the 2 matrices
    """
    return np.matmul(m_a, m_b)
