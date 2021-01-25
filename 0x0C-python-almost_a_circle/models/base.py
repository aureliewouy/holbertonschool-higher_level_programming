#!/usr/bin/python3
"""
Base class
"""
import os
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation list_objs to a file
        """
        newlist = []
        if list_objs is None:
            return newlist
        for obj in list_objs:
            newlist.append(obj.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instace with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        else :
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename):
            with open(filename, encoding = "utf-8") as f:
                content = f.read()
            objs = cls.from_json_string(content)
            newlist = []
            for obj in objs:
                new = cls.create(**obj)
                newlist.append(new)
            return newlist
        else:
            return []
