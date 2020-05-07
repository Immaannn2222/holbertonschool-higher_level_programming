#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        for key in a_dictionary.items():
            if a_dictionary == value:
                a_dictionary.pop(key)
        return(a_dictionary)
