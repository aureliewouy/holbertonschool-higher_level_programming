#!/usr/bin/python3
""" My integer """


class MyInt(int):
    """
    Class that inherits from int and invert operan ++ and !=
    """
    def __init__(self, myint):
        self.myint = myint

    def __eq__(self, other):
        return self.myint != other

    def __ne__(self, other):
        return self.myint == other
