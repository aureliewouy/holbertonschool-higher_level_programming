#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Function that appends a string a the end of a text file
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
    file.close()
    return len(text)
