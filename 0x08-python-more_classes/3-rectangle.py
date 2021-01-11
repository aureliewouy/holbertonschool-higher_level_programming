#!/usr/bin/python3
"""
Task 2 - Area and Perimeter

"""

class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialise Rectangle """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the reactangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        rect = ""
        if self.__width is 0 or self.__height is 0:
            return ""
        for i in range(self.__height):
           rect += ("#") * (self.__width) + ("\n")
        return rect[:-1]
