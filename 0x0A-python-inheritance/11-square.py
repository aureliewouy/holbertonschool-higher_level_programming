#!/usr/bin/python3
""" Task 11 - Square #2 """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        name = type(self).__name__
        return "[{}] {}/{}".format(name, self.__size, self.__size)
