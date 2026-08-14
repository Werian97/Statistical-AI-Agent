import ctypes
import unittest
from python_API import StatFuncs


class TestStringMethods(unittest.TestCase):

    def test_basic_usage(self):
        self.assertEqual(3, StatFuncs.mysum(1,2))

    def test_array(self):
        arr2 = ctypes.c_double * 2
        my_arr = arr2(2.0, -2.0)
        self.assertLess(abs(StatFuncs.mean(my_arr, 2)), 1e-6)

if __name__ == '__main__':
    unittest.main()