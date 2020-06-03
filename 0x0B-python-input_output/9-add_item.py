#!/usr/bin/python3
"""Python I/O"""
from sys import argv
import json


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


try:
    t = load_from_json_file("add_item.json")
except IOError:
    t = []
t += argv[1:]
save_to_json_file(t, "add_item.json")
