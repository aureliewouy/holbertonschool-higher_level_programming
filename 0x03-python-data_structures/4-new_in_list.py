#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    for i in my_list:
        new_list.append(i)
        if i == idx + 1:
            new_list.append(element)
            new_list.remove(i)
    if i < idx:
        return my_list
    return new_list
