import unittest
from agent.tools.get_fields import get_fields

class TestStringMethods(unittest.TestCase):
    def test_get_fields(self):
        fields: str = get_fields()
        self.assertEqual(
            fields,
            "date,price,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,street,city,statezip,price_per_sqft"
        )

    def test_get_fields_non_existing_file(self):
        alert_message: str = get_fields("./this_path_does_not_exists")
        self.assertEqual(
            alert_message,
            "./this_path_does_not_exists is not a valid file path"
        )

if __name__ == '__main__':
    unittest.main()