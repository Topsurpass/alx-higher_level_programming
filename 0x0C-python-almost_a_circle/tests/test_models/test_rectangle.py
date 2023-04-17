#!/usr/bin/python3

"""
This module contains test cases based on Rectangle class

The tests can be run using these commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_rectangle.py

Below are several test cases on the class
"""

import unittest
import os
import pep8
from io import StringIO
from models import rectangle
from contextlib import redirect_stdout

Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')


class TestRectangle(unittest.TestCase):
    """Several test cases for the rectangle class"""

    def setUp(self):
        """For dictionary conversion"""
        self.r_dict = Rectangle(2, 3, 4, 5, 6)

    def test_orderly_inpt_val(self):
        """Test input if correctly in order"""
        r1 = Rectangle(3, 2, 60, 10, 6)

        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 60)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 6)

    def test_default_val(self):
        """Test default values"""
        r2 = Rectangle(5, 4)

        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

    def test_wrong_input(self):
        """Test invalid inputs"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3], 3, 5, 3)
            Rectangle("20", 3, 3, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-18, 4, 5, 3)
            Rectangle(0, 5, 6, 3)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, "4")
            Rectangle(3, (3,), 4, 6)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4, 5, 6, 3)
            Rectangle(6, 0, 6, 3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, (3, 4))

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -5, 6, 3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 18, (7, 4))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 5, -6, 3)

    def test_priv_attr(self):
        """Test if attributes are private"""

        with self.assertRaises(AttributeError):
            print(Rectangle.width)
            print(Rectangle.height)
            print(Rectangle.x)
            print(Rectangle.y)
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_over_under_args(self):
        """Test for over and under arguments supplied"""

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 2, 3, 5, 6, 7)
            Rectangle()
            Rectangle(1)

    def test_to_dictionary(self):
        """Test to confirm dictionary"""

        dic = {"width": 2, "height": 3, "x": 4, "y": 5, "id": 6}
        my_type = self.r_dict.to_dictionary()
        self.assertEqual(my_type, dic)
        self.assertTrue(isinstance(my_type, dict))

    def test_obj_to_str(self):
        """Test object conversion to strig"""

        a = str(self.r_dict)
        strng = "[Rectangle] (6) 4/5 - 2/3"
        self.assertEqual(a, strng)
        self.assertEqual(type(a), str)

    def test_display(self):
        """Check if stdout display is equal"""

        check = "\n\n\n\n\n    ##\n    ##\n    ##\n"
        with StringIO() as buf, redirect_stdout(buf):
            self.r_dict.display()
            output = buf.getvalue()
        self.assertEqual(output, check)

        check2 = "\n\n\n   ####\n   ####\n   ####\n   ####\n"
        r4 = Rectangle(4, 4, 3, 3, 7)
        with StringIO() as buff, redirect_stdout(buff):
            r4.display()
            output_2 = buff.getvalue()
        self.assertEqual(output_2, check2)

    def test_area(self):
        """Check if area is correct"""
        self.assertEqual(self.r_dict.area(), 6)

    def test_update(self):
        """Test for updated attributes"""
        self.r_dict.update(3)
        self.assertEqual(str(self.r_dict), "[Rectangle] (3) 4/5 - 2/3")
        self.r_dict.update(3, 9)
        self.assertEqual(str(self.r_dict), "[Rectangle] (3) 4/5 - 9/3")
        self.r_dict.update(3, 9, 8)
        self.assertEqual(str(self.r_dict), "[Rectangle] (3) 4/5 - 9/8")
        self.r_dict.update(3, 9, 8, 11)
        self.assertEqual(str(self.r_dict), "[Rectangle] (3) 11/5 - 9/8")
        self.r_dict.update(3, 9, 8, 11, 1)
        self.assertEqual(str(self.r_dict), "[Rectangle] (3) 11/1 - 9/8")

        """Test for *kwargs"""
        self.r_dict.update(height=33, width=209, id=10)
        self.assertEqual(str(self.r_dict), "[Rectangle] (10) 11/1 - 209/33")
        self.r_dict.update(x=303, y=400)
        self.r_dict.update(
                str(self.r_dict), "[Rectangle] (10) 303/400 - 209/33]")
