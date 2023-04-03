#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):

    def tes_max(self):
        result = max_integer([1,2,3,4])
        result1 = max_integer([1,3,4,2])
        self.assertEqual(result, 4)
        self.assertEqual(resul1, 4)
