#!/usr/bin/python3
"""Inheritance"""


class BaseGeometry:
    """Raises exception of implementation"""
    def area(self):
        raise Exception("area() is not implemented")
