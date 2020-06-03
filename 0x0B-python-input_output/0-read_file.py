#!/usr/bin/python3
"""Python I/O"""


def read_file(filename=""):
    """read a file"""
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
