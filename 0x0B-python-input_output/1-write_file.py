#!/usr/bin/python3
"""
Write to a file
"""
def write_file(filename="", text=""):
    """
    Function that writes a string to a text file UTF8 and returns num of char
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
    file.close()
    return len(text)
