#!/usr/bin/python3
"""" square class"""


def print_square(size):
    """prints a square"""

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is False and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size):
            print('#', end='')
        print()
