from collections.abc import Callable
import os

HOUSE_PRICES: str = "small_data/house_prices.csv"
TEST_TABLE: str = "small_data/test_table.csv"
BIGGER_TEST_TABLE: str = "small_data/bigger_test_table.csv"
DATA_DIRECTORY: str = "./data"
TMP_FILEPATH: str = "./data/tmp"

def validate_filepath(target_table: str):
    if os.path.splitext(target_table)[1] != ".csv":
        return 'Error: Can access only files with ".csv" extension'
    
    workdir_abspath: str = os.path.abspath(DATA_DIRECTORY)
    target_table_path = os.path.normpath(os.path.join(workdir_abspath, target_table))

    valid_target_file = os.path.commonpath([workdir_abspath, target_table_path]) == workdir_abspath
    if not valid_target_file:
        return f'Error: Cannot open "{target_table}" as it is outside the permitted working directory'

    if not os.path.isfile(target_table_path):
        return f'Error: "{target_table}" does not exist'

    return target_table_path

def path_validator(func: Callable[..., str]):
    def inner_func(target_table: str, **kwargs):
        result: str = validate_filepath(target_table)
        if result[:6] == "Error:":
            return result
        return func(result, **kwargs)
    return inner_func
