#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    elif a_dictionary is {}:
        return None
    elif type(a_dictionary) is not dict:
        return None
    else:
        return max(a_dictionary)
