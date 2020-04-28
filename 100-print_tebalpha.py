#!/usr/bin/python3
for x in range(90, 64, -1):
    if x % 2 == 0:
        print("{:c}".format(x + 32), end="")
    else:
        print("{:c}".format(x), end="")
