#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if (ord(x) > 96) and (ord(x) < 123):
            y = ord(x) - 32
        else:
            y = ord(x)
        print("{}".format(chr(y)), end="")
    print("")
