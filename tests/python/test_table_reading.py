import unittest
from data import read_data

from data.read_data import Table

file_path: str = "./data/big_data/house_prices.csv"
table: Table = read_data.get_table(file_path)

class TestStringMethods(unittest.TestCase):
    def test_reading(self):
        self.assertEqual(table.rows[0][:3],
                         ['2014-05-02', '313000.0', '3.0'])
        self.assertEqual(table.fields[3:6],
                         ['bathrooms', 'sqft_living', 'sqft_lot'])

    def test_pick_rows(self):
        subtable: Table = table.pick_rows('bathrooms', '2')
        i: int = subtable.fields.index('bathrooms')
        for row in subtable.rows:
            self.assertEqual(row[i], '2')

        with self.assertRaises(ValueError):
            table.pick_rows('gardens', 'tall grass')

    def test_get_column(self):
        first_column: list[str] = table.get_column('date')
        self.assertEqual(first_column[:4],
                         ['2014-05-02', '2014-05-02', '2014-05-02', '2014-05-02'])

        with self.assertRaises(ValueError):
            non_existing_column = table.get_column('dates')

if __name__ == '__main__':
    unittest.main()