import unittest
from python_API import StatFuncs


class TestStringMethods(unittest.TestCase):

    def test_basic_usage(self):
        self.assertEqual(3, StatFuncs.mysum(1,2))

    def test_array(self):
        self.assertLess(abs(StatFuncs.mean([2.0,-2.0])), 1e-6)
        self.assertLess(abs(StatFuncs.mean([-3.0, -2.0, -1.0]) + 2), 1e-6)
        self.assertLess(abs(StatFuncs.mean([2.0]) - 2), 1e-6)

if __name__ == '__main__':
    unittest.main()