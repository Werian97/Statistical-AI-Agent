import unittest

from data import filter
from data import read_write_data

from data.read_write_data import Table

from data.filepath_to_data import HOUSE_PRICES, TEST_TABLE

house_prices: Table = read_write_data.get_table("./data/" + HOUSE_PRICES)
test_table: Table = read_write_data.get_table("./data/" + TEST_TABLE)

class TestStringMethods(unittest.TestCase):
    def test_reading(self):
        self.assertEqual(house_prices.rows[0][:3],
                         ['2014-05-02', '313000.0', '3.0'])
        self.assertEqual(house_prices.fields[3:6],
                         ['bathrooms', 'sqft_living', 'sqft_lot'])

    def test_get_column(self):
        first_column: list[str] = house_prices.get_column('date')
        self.assertEqual(first_column[:4],
                         ['2014-05-02', '2014-05-02', '2014-05-02', '2014-05-02'])

        with self.assertRaises(ValueError):
            non_existing_column = house_prices.get_column('dates')

    def test_add_tables(self):
        double_test_table = test_table + test_table
        self.assertEqual(len(double_test_table.rows), 6)
        self.assertEqual(double_test_table.rows[3][0], "2")
        self.assertEqual(double_test_table.rows[5], double_test_table.rows[2])

    def test_add_different_tables(self):
        with self.assertRaises(ValueError):
            err = test_table + house_prices

    def test_filter_by_exact_value(self):
        filtered_table: Table = filter.filter_by_exact_value(test_table, "b", "1")
        self.assertEqual(len(filtered_table.rows), 1)
        self.assertEqual(filtered_table.rows[0], ["3", "1", "yes", "0.02"])

        filtered_table2: Table = filter.filter_by_exact_value(test_table, "c", "yes")
        self.assertEqual(len(filtered_table.rows), 1)
        self.assertEqual(filtered_table2.rows[0], ["3", "1", "yes", "0.02"])

    def test_filter_by_numerical_range(self):
        filtered_table: Table = filter.filter_by_numerical_range(test_table, "a", 0, 4)
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.rows[0][0], "2")
        self.assertEqual(filtered_table.rows[1][0], "3")

    def test_filter_by_extreme_numerical_range(self):
        filtered_table: Table = filter.filter_by_numerical_range(test_table, "a", 0, float("+inf"))
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.rows[0][0], "2")
        self.assertEqual(filtered_table.rows[1][0], "3")

    def test_filter_by_numerical_range_non_float(self):
        with self.assertRaises(ValueError):
            filter.filter_by_numerical_range(test_table, "c", 0, 4)

    def test_filter_by_numerical_range_empty_table(self):
        with self.assertRaises(ValueError):
            filter.filter_by_numerical_range(test_table, "a", 3, 2)

    def test_filter_by_alphabetical_range(self):
        filtered_table: Table = filter.filter_by_alphabetical_range(test_table, "c", "-2", "1")
        self.assertEqual(len(filtered_table.rows), 1)
        self.assertEqual(filtered_table.rows[0][2], "0")

    def test_filter_by_alphabetical_range_empty_table(self):
        with self.assertRaises(ValueError):
            filter.filter_by_alphabetical_range(test_table, "c", "b", "a")

    def test_remove_exact_value(self):
        filtered_table: Table = filter.remove_exact_value(test_table, "b", "1")
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.get_column("a"), ["2", "-10"])

    def test_remove_exact_non_existing_value(self):
        with self.assertRaises(ValueError):
            filter.remove_exact_value(test_table, "b", "3")

    def test_remove_numerical_range(self):
        filtered_table: Table = filter.remove_numerical_range(test_table, "b", -2, 0.3)
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.get_column("a"), ["3", "-10"])

    def test_remove_numerical_range_non_intersecting_range(self):
        with self.assertRaises(ValueError):
            filter.remove_numerical_range(test_table, "b", -2, -1)

    def test_remove_alphabetical_range(self):
        filtered_table: Table = filter.remove_alphabetical_range(test_table, "b", "0", "2")
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.get_column("a"), ["2", "-10"])

    def test_remove_alphabetical_range_non_intersecting_range(self):
        with self.assertRaises(ValueError):
            filter.remove_alphabetical_range(test_table, "b", "-1", "3")

if __name__ == '__main__':
    unittest.main()
