from python_API import StatFuncs

from data.read_write_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_write_data import get_table
from data.filepath_to_data import path_validator

def get_column_mode_to_wrap(target_table: str, field: str):
    A: Table = get_table(target_table)
    column: list[str] = A.get_column(field)

    return str(StatFuncs.mode(column))

get_column_mode = path_validator(get_column_mode_to_wrap)

schema_get_column_mode: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_column_mode",
        "description": "Calculate the mode of the given column. In case there are multiple values with the same frequence this function will return the (alphabetical) biggest one.",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
                "field": {
                    "type": "string",
                    "description": "The corresponding column is the one whose mode will be computed"
                },
            },
            "required": ["target_table", "field"]
        },
    },
}
