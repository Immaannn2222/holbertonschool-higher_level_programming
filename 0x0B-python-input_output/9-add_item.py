#!/usr/bin/python3
import sys
import json


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
li = sys.argv[1:]

try:
    li = load_from_json_file("add_item.json")
except IOError:
    li += sys.argv[1:]
    save_to_json_file(old, "add_item.json")
