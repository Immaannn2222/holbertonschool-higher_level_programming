#!/usr/bin/python3
"""Inheritance"""


class MyInt(int):
    """rebel int"""
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x != other.x

    def __ne__(self, other):
        return not self.__eq__(other)
