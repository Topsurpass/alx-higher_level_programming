#!/usr/bin/python3

"""
This module contains test cases based on Square class

The tests can be run using these commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_square.py

Below are several test cases on the class
"""

import unittest
import pep8
from io import StringIO
from models import square
from contextlib import redirect_stdout

Square = square.Square


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')


class TestSquare(unittest.TestCase):
    """Several test cases for the square class"""

    def setUp(self):
        """For dictionary conversion"""
        self.r_dict = Square(2, 3, 4, 5)

    def test_orderly_inpt_val(self):
        """Test input if correctly in order"""
        r1 = Square(3, 2, 60, 10)

        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 60)
        self.assertEqual(r1.id, 10)

    def test_default(self):
        """Test default"""
        r2 = Square(1)

        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_default_val(self):
        """Test default values"""
        r2 = Square(5, 0, 0, 3)

        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 3)

    def test_wrong_input(self):
        """Test invalid inputs"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 3], 3, 5, 3)
            Square("20", 3, 3, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-18, 4, 5, 3)
            Square(0, 5, 6, 3)
            Square(-1)
            Square(0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, "4")
            Square(3, (3,), 4, 6)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -4, 5, 6)
            Square(6, 0, 6, 3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, (3, 4))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 4, -5, 6)

    def test_priv_attr(self):
        """Test if attributes are private"""

        with self.assertRaises(AttributeError):
            print(Square.width)
            print(Square.height)
            print(Square.x)
            print(Square.y)
            print(Square.__width)
            print(Square.__height)
            print(Square.__x)
            print(Square.__y)

    def test_over_under_args(self):
        """Test for over and under arguments supplied"""

        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 2, 3, 5, 6, 7)
            Square()
            Square(1)

    def test_to_dictionary(self):
        """Test to confirm dictionary"""

        dic = {"size": 2, "x": 3, "y": 4, "id": 5}
        my_type = self.r_dict.to_dictionary()
        self.assertEqual(my_type, dic)
        self.assertTrue(isinstance(my_type, dict))

    def test_obj_to_str(self):
        """Test object conversion to strig"""

        a = str(self.r_dict)
        strng = "[Square] (5) 3/4 - 2"
        self.assertEqual(a, strng)
        self.assertEqual(type(a), str)

    def test_display(self):
        """Check if stdout display is equal"""

        check = "\n\n\n\n   ##\n   ##\n"
        with StringIO() as buf, redirect_stdout(buf):
            self.r_dict.display()
            output = buf.getvalue()
        self.assertEqual(output, check)

        check2 = "\n\n\n    ####\n    ####\n    ####\n    ####\n"
        r4 = Square(4, 4, 3, 3)
        with StringIO() as buff, redirect_stdout(buff):
            r4.display()
            output_2 = buff.getvalue()
        self.assertEqual(output_2, check2)

    def test_area(self):
        """Check if area is correct"""
        self.assertEqual(self.r_dict.area(), 4)

    def test_update(self):
        """Test for updated attributes"""
        self.r_dict.update(3)
        self.assertEqual(str(self.r_dict), "[Square] (3) 3/4 - 2")
        self.r_dict.update(3, 9)
        self.assertEqual(str(self.r_dict), "[Square] (3) 3/4 - 9")
        self.r_dict.update(3, 9, 8)
        self.assertEqual(str(self.r_dict), "[Square] (3) 8/4 - 9")
        self.r_dict.update(3, 9, 8, 11)
        self.assertEqual(str(self.r_dict), "[Square] (3) 8/11 - 9")

        """Test for *kwargs"""
        self.r_dict.update(size=33, x=209, id=10)
        self.assertEqual(str(self.r_dict), "[Square] (10) 209/11 - 33")
        self.r_dict.update(x=303, y=400)
        self.assertEqual(str(self.r_dict), "[Square] (10) 303/400 - 33")
