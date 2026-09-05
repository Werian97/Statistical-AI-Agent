import unittest

from data import filter
from data import read_write_data

from data.read_write_data import Table

from data.filepath_to_data import HOUSE_PRICES, TEST_TABLE, BIGGER_TEST_TABLE, TMP_FILEPATH

house_prices: Table = read_write_data.get_table("./data/" + HOUSE_PRICES)
test_table: Table = read_write_data.get_table("./data/" + TEST_TABLE)
bigger_test_table: Table = read_write_data.get_table("./data/" + BIGGER_TEST_TABLE)

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

    def test_remove_numerical_range(self):
        filtered_table: Table = filter.remove_numerical_range(test_table, "b", -2, 0.3)
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.get_column("a"), ["3", "-10"])

    def test_remove_numerical_range_non_intersecting_range(self):
        with self.assertRaises(ValueError):
            filter.remove_numerical_range(test_table, "b", -2, 3)

    def test_remove_alphabetical_range(self):
        filtered_table: Table = filter.remove_alphabetical_range(test_table, "b", "00", "11")
        self.assertEqual(len(filtered_table.rows), 2)
        self.assertEqual(filtered_table.get_column("a"), ["2", "-10"])

    def test_remove_alphabetical_range_non_intersecting_range(self):
        with self.assertRaises(ValueError):
            filter.remove_alphabetical_range(test_table, "b", "-1", "3")

    def test_multiple_filters(self):
        filters_1: filter.Filters = {
            "exact_value": {
                "a": "3",
            },
        }
        filter.filter(bigger_test_table, filters_1)
        filtered_table_1: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_01.csv")
        self.assertEqual(len(filtered_table_1.rows), 1)

        filters_2: filter.Filters = {
            "numerical_range": {
                "b": {
                    "min_value": -100,
                    "max_value": 0
                },
            },
        }
        filter.filter(bigger_test_table, filters_2)
        filtered_table_2: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_02.csv")
        self.assertEqual(len(filtered_table_2.rows), 7)
        self.assertEqual(filtered_table_2.rows[1][1], "-22")
        
        filters_3: filter.Filters = {
            "alphabetical_range": {
                "c": {
                    "min_value": "0",
                    "max_value": "z"
                },
                "d": {
                    "min_value": "3",
                    "max_value": "z"
                }
            },
        }
        filter.filter(bigger_test_table, filters_3)
        filtered_table_3: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_03.csv")
        self.assertEqual(len(filtered_table_3.rows), 6)
        self.assertEqual(filtered_table_3.rows[2][3], "3")
                
        filters_4: filter.Filters = {
            "exact_value_remove": {
                "a": "7",
                "f": "6"
            },
        }
        filter.filter(bigger_test_table, filters_4)
        filtered_table_4: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_04.csv")
        self.assertEqual(len(filtered_table_4.rows), 9)
        self.assertEqual(filtered_table_4.rows[0][2], "-2")

                
        filters_5: filter.Filters = {
            "numerical_range_remove": {
                "a": {
                    "min_value": 1,
                    "max_value": 2,
                },
                "e": {
                    "min_value": -5,
                    "max_value": 3,
                },
            },
        }
        filter.filter(bigger_test_table, filters_5)
        filtered_table_5: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_05.csv")
        self.assertEqual(len(filtered_table_5.rows), 2)
        self.assertEqual(filtered_table_5.rows[1][4], "-22")

                
        filters_6: filter.Filters = {
            "alphabetical_range_remove": {
                "a": {
                    "min_value": "-5",
                    "max_value": "3",
                },
            },
        }
        filter.filter(bigger_test_table, filters_6)
        filtered_table_6: Table = read_write_data.get_table(TMP_FILEPATH + "/tmp_06.csv")
        self.assertEqual(len(filtered_table_6.rows), 8)
        self.assertEqual(filtered_table_6.rows[6][0], "-22")

        read_write_data.clean_temporary()


if __name__ == '__main__':
    unittest.main()
