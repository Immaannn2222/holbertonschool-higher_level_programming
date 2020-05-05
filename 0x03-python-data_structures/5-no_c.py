#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for character in my_string:
        if character not in 'Cc':
            new += character
    return new
