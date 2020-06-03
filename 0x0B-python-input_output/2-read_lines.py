#!/usr/bin/python3
"""Python I/O"""


def read_lines(filename="", nb_lines=0):
    """eads n lines of a text file"""
    co = 0
    with open(filename, "r") as fi:
        for line in fi:
            if co >= nb_lines or nb_lines < 0:
                break
            co += 1
            print(line, end="")
