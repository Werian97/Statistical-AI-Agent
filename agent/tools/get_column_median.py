from python_API import StatFuncs

from data.read_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_data import get_table
from data.filepath_to_data import path_validator

def get_column_median_to_wrap(target_table: str, field: str):
    A: Table = get_table(target_table)
    column: list[str] = A.get_column(field)
    try:
        column_f: list[float] = [float(x) for x in column]
    except Exception:
        return "Error: you can calculate median only for numerical values"

    return str(StatFuncs.median(column_f))

get_column_median = path_validator(get_column_median_to_wrap)

schema_get_column_median: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_column_median",
        "description": "Calculate the median of the given column. The values MUST be numerical",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
                "field": {
                    "type": "string",
                    "description": "The corresponding column is the one whose median will be computed"
                },
            },
            "required": ["target_table", "field"]
        },
    },
}
