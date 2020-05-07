#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    i = 0
    r = roman_string
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and a_dict[r[i]] < a_dict[r[i + 1]]:
            res -= a_dict[roman_string[i]]
        else:
            res += a_dict[roman_string[i]]
    return res
