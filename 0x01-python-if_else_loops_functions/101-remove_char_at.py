#!/usr/bin/python3
def remove_char_at(str, n):
newstr = str[:n] + str[n + 1:]
    for i in str:
        j = j + 1
        if j != n:
            return i
