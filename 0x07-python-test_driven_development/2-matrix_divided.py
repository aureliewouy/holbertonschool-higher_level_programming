#!/usr/bin/python3
"""

Task 1 - Divide a matrix

"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = []
    if isinstance(matrix, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if isinstance(i, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(i) is 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row = []
        for j in i:
            if isinstance(j, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row.append(round(float(j/div), 2))
        newmatrix.append(row)
    return newmatrix
