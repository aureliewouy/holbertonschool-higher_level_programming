#!/usr/bin/python3
"""
Unittest for the Rectangle class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        """
        Test with the id
        """
        test = Base(3)
        self.assertEqual(test.id, 3)

    def test_without_id(self):
        """
        Test without the id
        """
        test = Base()
        test2 = Base()
        self.assertEqual(test2.id, 2)

    def test_negative(self):
        """
        Test with negative id
        """
        test = Base(-1)
        self.assertEqual(test.id, -1)
