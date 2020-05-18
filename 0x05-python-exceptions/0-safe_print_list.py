#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for y in range(x):
                print("{}".format(my_list[y]), end="")
                count += 1
        print("")
        return count
    except IndexError:
        print("")
        return count
