import unittest

from agent.tools.get_fields import get_fields
from agent.tools.get_column_mean import get_column_mean
from data.filepath_to_data import HOUSE_PRICES, TEST_TABLE

class TestStringMethods(unittest.TestCase):
    def test_get_fields(self):
        fields: str = get_fields(HOUSE_PRICES)
        self.assertEqual(
            fields,
            "date,price,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,street,city,statezip,price_per_sqft"
        )

    def test_get_fields_without_csv_extension(self):
        alert_message: str = get_fields("./this_path_does_not_exist")
        self.assertEqual(
            alert_message,
            'Error: Can access only files with ".csv" extension'
        )

    def test_get_fields_non_existing_table(self):
        alert_message: str = get_fields("./this_file_does_not_exist.csv")
        self.assertEqual(
            alert_message,
            'Error: "./this_file_does_not_exist.csv" does not exist'
        )

    def test_get_column_mean(self):
        result: float = float(get_column_mean(TEST_TABLE, "a"))
        self.assertLessEqual(result + 1.666, 1e-6)

if __name__ == '__main__':
    unittest.main()