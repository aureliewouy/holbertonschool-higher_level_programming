#!/usr/bin/python3
"""
Base class
"""


class Base:
    """
    The base of all other classes
    The goal of it is to manage id attribute in all the future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
