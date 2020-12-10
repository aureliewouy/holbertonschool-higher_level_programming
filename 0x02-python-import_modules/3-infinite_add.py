#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = 0
    if len(argv) > 1:
        for i in argv[1:]:
            num = num + int(i)
    print("{:d}".format(num))
