#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list[:]
    for i in my_new_list:
        if i == search:
            my_new_list.insert(my_new_list.index(search), replace)
            my_new_list.remove(i)
    return my_new_list
