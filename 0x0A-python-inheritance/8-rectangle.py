#!/usr/bin/python3
""" Task 8 - Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initizalisation of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
