#!/usr/bin/python3
""" task 4 Square class """


class Square:
    """ a class square that defines a square """
    def __init__(self, size=0):
        """ Initialize Square"""
        self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout thr sqaure with the character # """
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
    @property
    def size(self):
        """ retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
