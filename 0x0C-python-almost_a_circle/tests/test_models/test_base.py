#!/usr/bin/python3
"""
Unittest for the Rectangle class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test for the Base class with Unittest
    """

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

    def test_to_json_string(self):
        """
        Test for the function to json string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), "[{\"id\": 12}]")

    def test_from_json_string(self):
        """
        Test for the function test from json string
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{ "id": 89}])

if __name__ == '__main__':
    unittest.main()
