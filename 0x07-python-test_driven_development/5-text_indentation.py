#!/usr/bin/python3
"""

Task 4 - Text identation

"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each  of these characters: ., ? and :
    """
    char = ".?:"
    newtext = ""
    flag = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for c in text:
        if flag == 1:
            if c == " ":
                continue
            else:
                flag = 0
        newtext = newtext + c
        for i in range(len(char)):
            if c == char[i]:
                newtext = newtext + "\n\n"
                flag = 1
    print("{}".format(newtext), end="")
