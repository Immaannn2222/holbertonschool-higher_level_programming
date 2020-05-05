#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list) is None:
        return None
    for i in my_list:
        i = 0
        if my_list[i] >= my_list[0]:
            i += 1
            max = my_list[i]
    return(max)
