import ctypes
import os
import unittest
from python_API import StatFuncs


class TestStringMethods(unittest.TestCase):

    def test_basic_usage(self):
        
        self.assertEqual(3, StatFuncs.mysum(1,2))

if __name__ == '__main__':
    unittest.main()