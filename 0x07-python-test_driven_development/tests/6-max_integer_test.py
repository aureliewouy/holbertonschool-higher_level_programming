#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

  def test_list(self):
      """
      test if the function find the maximum integer in a list
      """
      self.assertEqual(max_integer([1, 2, 3, 4]), 4)

  def test_float(self):
    """
    Test with float number
    """
    self.assertEqual(max_integer([1.89, 2.22, 3.45, 4.23]), 4.23)

  def test_empty(self):
    """
    Test the list is empty
    """
    self.assertEqual(max_integer([]), None)

  def test_double(self):
    """
    Test if there is multiple same value in a list
    """
    self.assertEqual(max_integer([34, 5, 34, 19, 0, 33, 34]), 34)

  def test_negative(self):
    """
    Test for the negative numbers
    """
    self.assertEqual(max_integer([-1, -2, -3]), -1)

  def test_one(self):
    """
    Test with one element in a list
    """
    self.assertEqual(max_integer([1]), 1)

  def test_char(self):
    """
    Test is there is a char in the list
    """
    self.assertRaises(TypeError, max_integer, [1, 2, 'y', 4])

  def test_string(self):
    """
    Test with one string
    """
    self.assertRaises(TypeError, max_integer, ["one", 2, 3, 4])

  def test_notlist(self):
    """
    Test if it's not a list
    """
    self.assertRaises(TypeError, max_integer, 123)

  def test_strings(self):
    """
    Test a list of strings
    """
    self.assertEqual(max_integer(["Hello", "Hi", "Good Morning"]), "Hi")

  def test_operand(self):
    """
    Test with operand
    """
    self.assertEqual(max_integer([1 - 3, 2 * 2 , 7 + 3]), 10)

if __name__ == '__main__':
    unittest.main()
