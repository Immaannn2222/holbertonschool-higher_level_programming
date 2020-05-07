#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    if a_dictionary is {}:
        return None
    else:
        return max(a_dictionary)
