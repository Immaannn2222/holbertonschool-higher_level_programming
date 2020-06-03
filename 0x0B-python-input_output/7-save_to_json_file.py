#!/usr/bin/python3
"""Python I/O"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using a JSON representation"""
    with open(filename, "w") as fi:
        fi.write(json.dumps(my_obj))
