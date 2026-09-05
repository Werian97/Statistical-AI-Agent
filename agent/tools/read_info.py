from openai.types.chat import ChatCompletionToolUnionParam

from data.read_write_data import read_dataset_info
from data.filepath_to_data import path_validator

def read_info_to_wrap(target_table: str):
    try:
        return read_dataset_info(target_table)
    except Exception as e:
        return str(e)

read_info = path_validator(read_info_to_wrap)

schema_read_info: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "read_info",
        "description": "Return a string containing a short description of the dataset and its fields.",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to read info of. All filepaths will be treated as relative to the 'data' directory.",
                },
            },
            "required": ["target_table"]
        },
    },
}
