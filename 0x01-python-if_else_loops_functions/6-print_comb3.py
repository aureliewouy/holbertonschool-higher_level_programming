#!/usr/bin/python3
for i in range(0, 100):
    first = i / 10
    last = i % 10
    if first < last:
        if i < 89:
            print("{:02d}".format(i), end=", ")
        if i == 89:
            print("{:d}".format(i))
