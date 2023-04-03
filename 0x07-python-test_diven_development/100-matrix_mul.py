#!/usr/bin/python3

"""
Module 100-matrix-mul
Ths module contains functions that multiply 2 matrices together
"""


def chk_row(row, strn):
    """This function checks individual rows in each matrix
    for errors
    Args:
        row: Individual row of each matrix
        strn: Name of the matrix in which the row failed
    Raises:
        TypeError: if row contains data type other than float and int
        ValueError: if row is empty
    """
    err = strn + " should contain only integers or floats"
    if len(row) == 0:
        raise ValueError(strn + " can't be empty")
    else:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err)


def deep_chk(mat, strn):
    """This function checks individual matrix for errors
    Args:
        mat: Matrix to check
        strn: Name of the failed matrix

    Raises:
        TypeError: if any of the matrix contains error
        ValueError: if matrix sizes are not the same
    """
    if len(mat) == 0:
        raise ValueError(strn + " can't be empty")
    for row in mat:
        if not isinstance(row, list):
            raise TypeError(strn + " must be a list of lists")
        else:
            a = len(mat[0])
            if len(row) != a:
                raise TypeError(
                        "each row of " + strn + " must be of the same size"
                        )
            else:
                chk_row(row, strn)


def matrix_mul(m_a, m_b):
    """This function multiply 2 matrices and return a new list
    or matrix containing the result of the product of the 2 matrices

    Args:
        m_a: First matrix
        m_b: Second matrix

    Raises:
        TypeError: m_a or m_b is not a list or they contains data type
        other than int and float or when both rows are not the same

        ValueError: m_a or m_b is an empty list or both can't be multiplied

    Return: The product of the 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    else:
        deep_chk(m_a, "m_a")
        deep_chk(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    for a in range(len(m_a)):
        for b in range(len(m_b[0])):
            for c in range(len(m_b)):
                result[a][b] += m_a[a][c] * m_b[c][b]

    return result
