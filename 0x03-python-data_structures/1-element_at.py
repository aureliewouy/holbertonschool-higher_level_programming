#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if i == idx + 1:
            return i
    if i < idx:
        return None
