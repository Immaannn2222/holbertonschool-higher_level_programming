#!/usr/bin/python3
"""Python I/O"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”"""
    with open(filename, "r") as fi:
        return (json.load(fi))
