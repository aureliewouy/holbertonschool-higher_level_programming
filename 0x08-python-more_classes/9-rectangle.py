#!/usr/bin/python3
"""
Task 9 - A square is a rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialise Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        type(self).print_symbol

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
        """
        Using __str__ method for string representation of the reactangle
        """
        rect = ""
        if self.__width is 0 or self.__height is 0:
            return ("")

        for i in range(self.__height):
            rect += (str(self.print_symbol)) * (self.__width) + ('\n')
        return (rect[:-1])

    def __repr__(self):
        """
        Returns printable representation or the reactangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print the message when is deleted"
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggedt rectangle based on the area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance
        """
        return cls(size, size)
