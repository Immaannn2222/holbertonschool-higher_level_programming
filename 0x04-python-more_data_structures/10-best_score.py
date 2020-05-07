#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) is 0:
        return None
    else:
        return(max(a_dictionary))
