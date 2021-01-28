#!/usr/bin/python3
"""
Unittest for the Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test for the Square class with unittest
    """
    def test_size(self):
        """
        Test initialize the class Square with the size
        """
        test = Square(2)
        self.assertEqual(test.size, 2)

    def test_raise_type(self):
        """Testing TypeError """
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_raise_value(self):
        """ Testing ValueError """
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        """
        Test the area function with the square class
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_update(self):
        """
        Test for the update method of the Square class
        """
        s1 = Square(5)
        s1.update(10)
        s1.update(1, 2, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1),"[Square] (1) 3/4 - 2")


    def test_upkwargs(self):
        """
        Test the update with the kwargs
        """
        s1 = Square(5)
        s1.update(x=12)
        s1.update(size=7, y=1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1),"[Square] (89) 12/1 - 7")

    def test_save(self):
        """ Testing save_to_file method """
        test = Square.save_to_file([Square(1)])
        self.assertEqual(test, None)
        self.assertEqual(Square.save_to_file([]), None)

    def test_create(self):
        """ Testing create method """
        test1 = Square(1, 9, 3)
        test1_dict = test1.to_dictionary()
        test2 = Square.create(**test1_dict)
        self.assertEqual(type(test2), type(test2))

if __name__ == '__main__':
    unittest.main()
