#!/usr/bin/python3
"""Python I/O"""


def append_write(filename="", text=""):
    """appends a string at the end returns the number of chara"""
    with open(filename, "a") as fi:
        return (fi.write(text))
