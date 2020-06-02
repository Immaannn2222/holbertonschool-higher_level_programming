#!/usr/bin/python3
"""Inheritnace"""


class MyList(list):
    """inherted from list"""

    def print_sorted(self):
        print(sorted(self))
