#!/usr/bin/python3
"""Python I/O"""


def number_of_lines(filename=""):
    """number of lines"""
    co = 0
    with open(filename, encoding="utf-8") as fi:
        for line in fi:
            co += 1
        return co
