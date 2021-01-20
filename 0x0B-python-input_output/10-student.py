#!/usr/bin/python3
"""
My class Student that defines a student
"""


class Student:
    """ Class student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new[key] = value
        return new
