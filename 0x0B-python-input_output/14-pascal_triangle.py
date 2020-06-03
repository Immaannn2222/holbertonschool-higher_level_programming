#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return

    for l in range(1, n + 1):
        c = 1
        for x in range(1, l + 1):
            print(c, end=" ")
            c = int(c * (l - x) / x)
        print("")
