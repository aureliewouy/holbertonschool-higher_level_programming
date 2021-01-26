#!/usr/bin/python3
"""base module model"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the width height x and y
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the reactangle """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        name = type(self).__name__
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return ("[{}] ({}) {}/{} - {}/{}".format(name, i, x, y, w, h))

    def update(self, *args, **kwargs):
        nb = len(args);
        if nb > 0:
            self.id = args[0]
        if nb > 1:
            self.width = args[1]
        if nb > 2:
            self.height = args[2]
        if nb > 3:
            self.x = args[3]
        if nb > 4:
            self.y = args[4]
        if kwargs is not None:
            if "id" in kwargs.keys():
                self.id = kwargs.get('id')
            if "width" in kwargs.keys():
                self.width = kwargs.get('width')
            if "height" in kwargs.keys():
                self.height = kwargs.get('height')
            if "x" in kwargs.keys():
                self.x = kwargs.get('x')
            if "y" in kwargs.keys():
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Reactangle
        """
        to_dict = {'id' : self.id,
                   'width' : self.width,
                   'height' : self.height,
                   'x' : self.x,
                   'y' : self.y}
        return to_dict
