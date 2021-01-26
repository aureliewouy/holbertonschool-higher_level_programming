#!/usr/bin/python3
"""
Unittest for the Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test for the Rectangle class  with unittest
    """

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
        self.assertEqual(test.y, 0)

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

    def test_area(self):
        """
        Test the area public function
        """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_str(self):
        """
        Test the str method
        """
        r1 = Rectangle(2, 2, 1, 1, 15)
        self.assertEqual(str(r1), "[Rectangle] (15) 1/1 - 2/2")

    def test_update(self):
        """
        Test for the uptade method
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_up_kwargs(self):
        """
        Test for kwargs
        """
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(height=1)
        r2.update(width=1, x=2)
        r2.update(y=1, width=2, x=3, id=90)
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), "[Rectangle] (90) 1/3 - 4/2")
"""
    def test_todict(self):
        """
   """     Test for the to_dictionary() function
        """
     """   r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), )
"""

if __name__ == '__main__':
    unittest.main()
