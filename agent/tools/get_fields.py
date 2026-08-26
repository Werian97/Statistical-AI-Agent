from data.filepath_to_data import HOUSE_PRICES

from data.read_data import Table
from openai.types.chat import ChatCompletionToolUnionParam

from data.read_data import get_table

def get_fields(filepath=HOUSE_PRICES) -> str:
    try:
        table: Table = get_table(filepath)
    except ValueError:
        return f"{filepath} is not a valid file path"
    return ",".join(table.fields)

schema_get_fields: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "get_fields",
        "description": "Return a string containing all the fields of the table separated by a comma.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "Filepath to the csv file to read. Default is the house_prices.csv",
                },
            },
        },
    },
}