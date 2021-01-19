#!/usr/bin/python3
""" Task 4 - Only sub class of """


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited from
    the specified class otherwise False
    """
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
