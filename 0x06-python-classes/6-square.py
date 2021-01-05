#!/usr/bin/python3
""" task 6 Square class """


class Square:
    """ a class square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize Square"""
        self.__size = size
        self.__position = position

    def area(self):
        """ Returns the area of the square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position fo square """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for n in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
