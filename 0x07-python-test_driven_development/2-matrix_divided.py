#!/usr/bin/python3
""" matrix module"""


def matrix_divided(matrix, div):
    """ divides all els of a mtrix"""

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if type(matrix) is not list:
            raise TypeError(te)
    leng = len(matrix[0])
    new = []
    for x in matrix:
        te = "matrix must be a matrix (list of lists) of integers/floats"
        if type(x) is not list:
            raise TypeError(te)
        if len(x) != leng:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError(te)
            return [[round(y / div, 2) for y in x] for x in matrix]
