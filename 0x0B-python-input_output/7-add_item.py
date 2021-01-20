#!/usr/bin/python3
"""
Load, add, save
"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list = []
i = 1
if len(argv) > 1:
    while i < len(argv):
        list.append(argv[i])
        i += 1

save_to_json_file(list, "add_item.json")
load_from_json_file("add_item.json")
