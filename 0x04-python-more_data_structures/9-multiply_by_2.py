#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = a_dictionary.copy()
        for key, value in new.items():
            new[key] = value * 2
        return new
