from python_API import StatFuncs

from data.read_write_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_write_data import get_table
from data.filepath_to_data import path_validator

def get_column_variance_to_wrap(target_table: str, field: str):
    A: Table = get_table(target_table)
    column: list[str] = A.get_column(field)
    try:
        column_f: list[float] = [float(x) for x in column]
    except Exception:
        return "Error: you can calculate variance only for numerical values"

    return str(StatFuncs.variance(column_f))

get_column_variance = path_validator(get_column_variance_to_wrap)

schema_get_column_variance: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_column_variance",
        "description": "Calculate the variance of the given column. The values MUST be numerical",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
                "field": {
                    "type": "string",
                    "description": "The corresponding column is the one whose variance will be computed"
                },
            },
            "required": ["target_table", "field"]
        },
    },
}
