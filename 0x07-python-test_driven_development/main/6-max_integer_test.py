#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):
    
    def test_max(self):
        result = max_integer([1,2,3,4])
        result1 = max_integer([1,3,4,2])
        result2 = max_integer([-100,3,-454, 2.4])
        self.assertEqual(result, 4)
        self.assertEqual(result1, 4)
        self.assertEqual(result2, 3)
