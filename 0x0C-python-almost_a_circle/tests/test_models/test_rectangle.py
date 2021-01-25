#!/usr/bin/python3
"""
Unittest for the Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width_height(self):
        """
        Test initialize the class with only width and height
        """
        test = Rectangle(10, 2)
        self.assertEqual(test.height, 2)
        self.assertEqual(test.width, 10)

    def test_no_xy(self):
        """
        Test without x and y
        """
        test = Rectangle(23, 33)
        self.assertEqual(test.x, 0)

    def test_xy(self):
        """
        Test with x declare
        """
        test = Rectangle(5, 2, 9)
        self.assertEqual(test.x, 9)

    def test_y(self):
        """
        Test with the y
        """
        test = Rectangle(5, 2, 3, 6)
        self.assertEqual(test.y, 6)

    def test_all(self):
        """
        Test initialize the class with all the parameters
        """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.height, 2)

    def test_type(self):
        """
        Test if is not an integer
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle(10, 3, 7, [1])
        with self.assertRaises(TypeError):
            Rectangle(10, 3, 1.4, 1)
        with self.assertRaises(TypeError):
            Rectangle(True, 3, 6, 1)

    def test_negative(self):
        """
        Test with negative number
        """
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 1)
        with self.assertRaises(ValueError):
            Rectangle(10, -2, 3, 1)

    def test_none(self):
        """
        Test without value
        """
        with self.assertRaises(TypeError):
            Rectangle()
