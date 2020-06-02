#!/usr/bin/python3
"""Inheritance"""
Rectangle = __import__("9-rectangle.py").Rectangle


def __init__(self, size):
    """Instantiation of size"""
    self.integer_validator("size", size)
    self.__size = size
