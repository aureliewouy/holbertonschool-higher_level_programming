#!/usr/bin/python3
from models.rectangle import Rectangle

"""
And now, the Square !
"""


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = type(self).__name__
        i = self.id
        x = self.x
        y = self.y
        s = self.size
        return ("[{}] ({}) {}/{} - {}".format(name, i, x, y, s))

    @property
    def size(self):
        """ retrieve the size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update function
        """
        nb = len(args);
        if nb > 0:
            self.id = args[0]
        if nb > 1:
            self.width = args[1]
        if nb > 2:
            self.x = args[2]
        if nb > 3:
            self.y = args[3]
        if kwargs is not None:
            if "id" in kwargs.keys():
                self.id = kwargs.get('id')
            if "size" in kwargs.keys():
                self.size = kwargs.get('size')
            if "x" in kwargs.keys():
                self.x = kwargs.get('x')
            if "y" in kwargs.keys():
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        to_dict = {'id' : self.id,
                   'size' : self.size,
                   'x' : self.x,
                   'y' : self.y}
        return to_dict
