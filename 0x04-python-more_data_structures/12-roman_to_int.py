#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is not str or len(roman_string) is 0:
        return None
    else:
        for key, value in a_dict.items():
            for i in roman_string:
                if i == a_dict[key]:
                    res += value
                else:
                    i += 1
    return res
