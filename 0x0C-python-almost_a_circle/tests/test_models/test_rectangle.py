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
        self.assertEqual(test.id, 1)

    def test_all(self):
        """
        Test initialize the class with all the parameters
        """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.width, 1)

