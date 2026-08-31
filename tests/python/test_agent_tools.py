import unittest

from agent.tools.call_functions import function_map

from data.filepath_to_data import HOUSE_PRICES, TEST_TABLE

get_fields = function_map["get_fields"]
get_column_mean = function_map["get_column_mean"]
get_column_max = function_map["get_column_max"]
get_column_min = function_map["get_column_min"]
get_column_variance = function_map["get_column_variance"]
get_column_covariance = function_map["get_column_covariance"]
get_column_median = function_map["get_column_median"]

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
        result: float = float(get_column_mean(TEST_TABLE, field ="a"))
        self.assertLessEqual(result + 1.666, 1e-6)

    def test_get_column_mean_non_numerical(self):
        alert_message: str = get_column_mean(TEST_TABLE, field ="c")
        self.assertEqual(
            alert_message,
            "Error: you can calculate mean only for numerical values"
        )

    def test_get_column_max(self):
        result: str = get_column_max(TEST_TABLE, field="a")
        self.assertEqual(result, "3.0")

    def test_get_column_max_non_numerical(self):
        alert_message: str = get_column_max(TEST_TABLE, field ="c")
        self.assertEqual(
            alert_message,
            "Error: you can calculate max only for numerical values"
        )

    def test_get_column_min(self):
            result: str = get_column_min(TEST_TABLE, field="a")
            self.assertEqual(result, "-10.0")
    
    def test_get_column_min_non_numerical(self):
        alert_message: str = get_column_min(TEST_TABLE, field ="c")
        self.assertEqual(
            alert_message,
            "Error: you can calculate min only for numerical values"
        )

    def test_get_column_variance(self):
            result: str = get_column_variance(TEST_TABLE, field="a")
            self.assertLess(abs(float(result) - 34.8888888), 1e-6)
    
    def test_get_column_variance_non_numerical(self):
        alert_message: str = get_column_variance(TEST_TABLE, field ="c")
        self.assertEqual(
            alert_message,
            "Error: you can calculate variance only for numerical values"
        )

    def test_get_column_covariance(self):
            result: str = get_column_covariance(TEST_TABLE, field1="a", field2="b")
            self.assertLess(abs(float(result) + 4.0), 1e-6)
    
    def test_get_column_covariance_non_numerical(self):
        alert_message: str = get_column_covariance(TEST_TABLE, field1 ="c", field2="d")
        self.assertEqual(
            alert_message,
            "Error: you can calculate covariance only for numerical values"
        )

    def test_get_column_median(self):
            result: str = get_column_median(TEST_TABLE, field="a")
            self.assertEqual(result, "2.0")
    
    def test_get_column_median_non_numerical(self):
        alert_message: str = get_column_median(TEST_TABLE, field="c")
        self.assertEqual(
            alert_message,
            "Error: you can calculate median only for numerical values"
        )

if __name__ == '__main__':
    unittest.main()