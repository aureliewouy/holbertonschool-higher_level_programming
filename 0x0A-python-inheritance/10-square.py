#!/usr/bin/python3
""" Task 10 - Square #1 """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
