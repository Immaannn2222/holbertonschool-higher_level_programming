#!/usr/bin/python3
"""Python I/O"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file"""
    co = 0
    with open(filename) as fi:
        li = fi.readlines()
        for co in range(len(li)):
            if co == nb_lines and nb_lines != 0:
                break
            print(li[co], end="")
