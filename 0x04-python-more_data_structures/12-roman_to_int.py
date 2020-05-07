#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key, value in a_dict.items():
        for i in roman_string:
            if i == key:
                res += value
    return res
