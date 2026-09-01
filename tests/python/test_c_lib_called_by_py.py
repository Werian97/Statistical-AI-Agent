import unittest
from python_API import StatFuncs

arr1: list[float] = [2.0,-2.0]
arr2: list[float] = [-3.0, -2.0, -1.0]
arr3: list[float] = [2.0]
class TestStringMethods(unittest.TestCase):

    def test_basic_usage(self):
        self.assertEqual(3, StatFuncs.mysum(1,2))

    def test_mean(self):
        self.assertLess(abs(StatFuncs.mean(arr1)), 1e-6)
        self.assertLess(abs(StatFuncs.mean(arr2) + 2), 1e-6)
        self.assertLess(abs(StatFuncs.mean(arr3) - 2), 1e-6)

    def test_max(self):
        self.assertEqual(StatFuncs.max(arr1), 2.0)
        self.assertEqual(StatFuncs.max(arr2), -1.0)
        self.assertEqual(StatFuncs.max(arr3), 2.0)
        self.assertEqual(StatFuncs.max([]), float("-inf"))

    def test_min(self):
        self.assertEqual(StatFuncs.min(arr1), -2.0)
        self.assertEqual(StatFuncs.min(arr2), -3.0)
        self.assertEqual(StatFuncs.min(arr3), 2.0)
        self.assertEqual(StatFuncs.min([]), float("+inf"))

    def test_variance(self):
        self.assertLess(abs(StatFuncs.variance(arr1) - 4.0), 1e-6)
        self.assertLess(abs(StatFuncs.variance(arr2) - 0.6666666), 1e-6)
        self.assertLess(abs(StatFuncs.variance(arr3)), 1e-6)

    def test_covariance(self):
        self.assertLess(abs(StatFuncs.covariance(arr1, arr1) - 4.0), 1e-6)
        self.assertLess(abs(StatFuncs.covariance(arr1, arr2[:2]) + 1), 1e-6)
        self.assertLess(abs(StatFuncs.covariance(arr3, arr1[:1])), 1e-6)
        self.assertLess(abs(StatFuncs.covariance([2.0, 3.0, -10.0], [0.0, 1.0, 2.0]) + 4.0), 1e-6)

    def test_covariance_different_length(self):
        with self.assertRaises(ValueError):
            StatFuncs.covariance(arr1, arr2)

    def test_median(self):
        self.assertLess(abs(StatFuncs.median(arr1)), 1e-6)
        self.assertEqual(StatFuncs.median(arr2), -2.0)
        self.assertEqual(StatFuncs.median(arr3), 2.0)

    def test_mode(self):
        arr_str: list[str] = ["aaa", "bb", "aaa", "aaa", "bb", "bb", "bb"]
        self.assertEqual(StatFuncs.mode(arr_str), "bb")
        arr_str = ["a", "b", "c", "d"]
        self.assertEqual(StatFuncs.mode(arr_str), "a")
        arr_str = ["b", "c", "a", "d"]
        self.assertEqual(StatFuncs.mode(arr_str), "a")
        arr_str = ["1", "2", "3"]
        self.assertEqual(StatFuncs.mode(arr_str), "1")
        arr_str = ["2", "3", "111111"]
        self.assertEqual(StatFuncs.mode(arr_str), "111111")

if __name__ == '__main__':
    unittest.main()