#!/usr/bin/python3
"""N queens in chess"""
import sys

if __name__ == "__main__":
    """checks the rules"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if isinstance(sys.argv[1], int) is False:
        raise TypeError("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
