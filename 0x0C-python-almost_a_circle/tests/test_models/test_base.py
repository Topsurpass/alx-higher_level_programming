#!/usr/bin/python3

"""
This module contains test cases of Base class

The tests can be run using these commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base.py

Below are several test cases on the class
"""
import json
import csv
import unittest
import os
import pep8
from models import base
from models import rectangle
from models import square

Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')

    def setUp(self):
        """Test setup"""
        pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")

        except FileNotFoundError:
            pass

    def test_default_id(self):
        """Test default id value"""
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(4).id, 4)
        self.assertEqual(Base(89).id, 89)

    def test_over_attr(self):
        """Test for too many arguments passed"""
        with self.assertRaises(TypeError):
            Base(1, 2)
            Base(1, 2, 3, 4)

    def test_class(self):
        """Test for class"""
        self.assertTrue(isinstance(Base(88), Base))

    def test_private_attr(self):
        """Test private attribute"""
        with self.assertRaises(AttributeError):
            Base(10).__nb_objects
            Base(11).nb_objects

    def test_to_json_string(self):
        """Test conversion of list of dictionary to json string"""

        r1 = {"id": 9, "width": 1, "height": 2, "x": 3, "y": 4}
        r2 = {"id": 19, "width": 11, "height": 12, "x": 13, "y": 14}
        compare = [
                {"id": 9, "width": 1, "height": 2, "x": 3, "y": 4},
                {"id": 19, "width": 11, "height": 12, "x": 13, "y": 14}]
        j_str = Base.to_json_string([r1, r2])

        self.assertTrue(j_str, compare)
        self.assertTrue(isinstance(j_str, str))
        self.assertTrue(isinstance(r1, dict))

    def test_none_to_json_string(self):
        """Test none conversion to json string"""
        r3 = None
        j_str = Base.to_json_string([r3])
        self.assertTrue(j_str, "[]")
        self.assertTrue(isinstance(j_str, str))

    def test_from_json_string(self):
        """Test from json string to list of dict"""
        j_str = '[{"id": 9, "width": 1, "height": 2, "x": 3, "y": 4},\
                {"id": 19, "width": 11, "height": 12, "x": 13, "y": 14}]'

        p_dict = Base.from_json_string(j_str)
        self.assertTrue(isinstance(p_dict, list))
        self.assertEqual(
                p_dict[0], {"id": 9, "width": 1, "height": 2, "x": 3, "y": 4})

    def test_create(self):
        """Test dictionary to an instance"""
        r1 = Rectangle(1, 2, 3, 4, 10)

        r_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r_dic)

        self.assertEqual(str(r1), '[Rectangle] (10) 3/4 - 1/2')
        self.assertEqual(str(r2), '[Rectangle] (10) 3/4 - 1/2')
        self.assertIsNot(r1, r2)

        new = Square.create(**{'id': 89})
        self.assertEqual(str(new), '[Square] (89) 0/0 - 2')

        r = Square(**{'id': 89, 'size': 1})
        self.assertEqual(str(r), '[Square] (89) 0/0 - 1')

        r3 = Square(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(r3), '[Square] (89) 2/0 - 1')

        r4 = Square(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(r4), '[Square] (89) 2/3 - 1')

    def test_save_to_file(self):
        """Test save to json file"""
        r1 = Rectangle(1, 2, 3, 4, 10)
        r2 = Rectangle(11, 12, 13, 14, 110)

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                    f.read(),
                    json.dumps(
                        [r1.to_dictionary(), r2.to_dictionary()]))

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(
                    f.read(),
                    json.dumps(
                        [{"id": 5, "size": 1, "x": 0, "y": 0}]))

    def test_save_none_to_file(self):
        """Test save to file"""
        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_save_empty_to_file(self):
        """Test save to file"""
        Rectangle.save_to_file([])
        Square.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_load_from_file(self):
        """Test load from json file"""

        r1 = Rectangle(1, 2, 3, 4, 10)
        r2 = Rectangle(11, 12, 13, 14, 110)

        Rectangle.save_to_file([r1, r2])
        frm_fil = Rectangle.load_from_file()

        self.assertEqual(len(frm_fil), 2)

        for i, k in enumerate(frm_fil):
            if i == 0:
                self.assertEqual(
                        str(k), '[Rectangle] (10) 3/4 - 1/2')
            if i == 1:
                self.assertEqual(
                        str(k), '[Rectangle] (110) 13/14 - 11/12')

        frm_sqr = Square.load_from_file()
        self.assertEqual(len(frm_sqr), 0)

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        frm_fil = Rectangle.load_from_file()
        self.assertTrue(isinstance(frm_fil, list))
        self.assertEqual(len(frm_fil), 0)
