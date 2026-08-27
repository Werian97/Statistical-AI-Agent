from python_API import StatFuncs

from data.read_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_data import get_table
from data.filepath_to_data import path_validator

def get_column_mean_to_wrap(target_table: str, field: str):
    A: Table = get_table(target_table)
    column: list[str] = A.get_column(field)
    try:
        column_f: list[float] = [float(x) for x in column]
    except Exception:
        return "Error: you can calculate mean only for numerical values"

    return str(StatFuncs.mean(column_f))

get_column_mean = path_validator(get_column_mean_to_wrap)

schema_get_column_mean: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_column_mean",
        "description": "Calculate the mean of the given column. The values MUST be numerical",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
                "field": {
                    "type": "string",
                    "description": "The corresponding column is the one whose mean will be computed"
                },
            },
            "required": ["target_table", "field"]
        },
    },
}
