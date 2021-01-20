#!/usr/bin/python3
"""
Read file
"""

def read_file(filename=""):
    """
    Function that reads a text file UTF8 and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
    file.close()
