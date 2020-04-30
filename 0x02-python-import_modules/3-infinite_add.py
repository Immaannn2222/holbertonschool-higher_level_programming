#!/usr/bin/python3
from sys import argv
j = 0
if __name__ == "__main__":
    for i in range(1, len(argv)):
        j += int(argv[i])
    print("{}".format(j))
