#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, vall in a_dictionary.items():
        if vall == value:
            del a_dictionary[k]
        return(a_dictionary)
