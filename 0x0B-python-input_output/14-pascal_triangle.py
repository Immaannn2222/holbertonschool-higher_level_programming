#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle of n"""
    triangle = []
    if n <= 0:
        return triangle

        triangle[0] = 1
    for l in range(1, n + 1):
        for x in range(1, l + 1):
            c = int(c * (l - x) / x)
        triangle[l].appen(c)
    return triangle
