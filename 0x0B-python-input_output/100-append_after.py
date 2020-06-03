#!/usr/bin/python3
"""Python I/O"""


def append_after(filename="", search_string="", new_string=""):
    """ """
    t = ""
    with open(filename) as fi:
        for line in fi:
            t += line
            if search_string in line:
                t += new_string
    with open(filename, "w") as fi:
        fi.write(t)
