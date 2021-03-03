#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
id2 = 18
id3 = -2
print("Element at index id2  {:d} is {}".format(id2, element_at(my_list, id2)))
print("Element at index id2 {:d} is {}".format(id3, element_at(my_list, id3)))
