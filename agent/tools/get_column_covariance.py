from python_API import StatFuncs

from data.read_write_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_write_data import get_table
from data.filepath_to_data import path_validator

def get_column_covariance_to_wrap(target_table: str, field1: str, field2: str):
    A: Table = get_table(target_table)
    column1: list[str] = A.get_column(field1)
    column2: list[str] = A.get_column(field2)
    try:
        column1_f: list[float] = [float(x) for x in column1]
        column2_f: list[float] = [float(x) for x in column2]
    except Exception:
        return "Error: you can calculate covariance only for numerical values"
    
    return str(StatFuncs.covariance(column1_f, column2_f))

get_column_covariance = path_validator(get_column_covariance_to_wrap)

schema_get_column_covariance: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_column_covariance",
        "description": "Calculate the covariance of the two given column. The values MUST be numerical in both columns",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
                "field1": {
                    "type": "string",
                    "description": "One of the two column whose covariance will be computed"
                },
                "field2": {
                    "type": "string",
                    "description": "One of the two column whose covariance will be computed"
                },
            },
            "required": ["target_table", "field1", "field2"]
        },
    },
}
