#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for x in range(len(str)):
        if x != n:
            s += str[x]
    return (s)
