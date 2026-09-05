from data.read_write_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_write_data import get_table
from data.filepath_to_data import path_validator

def get_fields_to_wrap(target_table) -> str:
    table: Table = get_table(target_table)
    return ",".join(table.fields)

get_fields = path_validator(get_fields_to_wrap)

schema_get_fields: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_fields",
        "description": "Return a string containing all the fields of the table separated by a comma.",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. All filepaths will be treated as relative to the 'data' directory.",
                },
            },
            "required": ["target_table"]
        },
    },
}
