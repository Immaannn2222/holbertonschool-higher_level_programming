#!/usr/bin/python3
"""Python I/O"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of chara"""
    co = 0
    with open(filename, "w") as fi:
        co = fi.write(text)
    return co
