from data.read_write_data import Table
from openai.types.chat import ChatCompletionToolUnionParam
from data.filter import Filters

from data.read_write_data import get_table
from data.filter import filter
from data.filepath_to_data import path_validator

def filter_data_to_wrap(target_table: str, filters: Filters):
    A: Table = get_table(target_table)
    try:
        new_file: str = filter(A, filters)
    except Exception as e:
        return str(e)

    return f"The file has been successfully created at this file path: {new_file}"

filter_data = path_validator(filter_data_to_wrap)

schema_filter_data: ChatCompletionToolUnionParam = {
    "type": "function",
    "function": {
        "name": "filter_data",
        "description": "Filter the target table using the filters you provide. If the result is not an empty table, it will be saved in './data/tmp'. The function return the new file path",
        "parameters": {
            "type": "object",
            "properties": {
                "target_table": {
                    "type": "string",
                    "description": "Filepath to the csv file to filter. All filepaths will be treated as relative to the 'data' directory.",
                },
                "filters": {
                    "type": "object",
                    "properties": {
                        "exact_value": {
                            "type": "object",
                            "description": " Each pair 'key:value' is treated as 'field:value-to-select'. Pick only the rows which contain the selected value in the selected field. The values are considered to be strings, so, for example 0 != 0.0",
                            "additionalProperties": {
                                "type": "string"
                            },
                        },
                        "numerical_range": {
                            "type": "object",
                            "description": "Each key identifies a field. Its value specifies the minimum and maximum values allowed for that field. Pick only the rows which have the selected field between the min_value and max_value selected. Min and max are excluded and the values in the field must be numerical.",
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "min_value": {
                                        "type": "number",
                                    },
                                    "max_value": {
                                        "type": "number",
                                    },
                                },
                                "required": ["min_value", "max_value"],
                                "additionalProperties": False
                            }
                        },
                        "alphabetical_range": {
                            "type": "object",
                            "description": "Each key identifies a field. Its value specifies the minimum and maximum values allowed for that field. Pick only the rows which have the selected field alphabetically between the min_value and max_value selected. Min and max are excluded",
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "min_value": {
                                        "type": "string",
                                    },
                                    "max_value": {
                                        "type": "string",
                                    },
                                },
                                "required": ["min_value", "max_value"],
                                "additionalProperties": False
                            }
                        },
                        "exact_value_remove": {
                            "type": "object",
                            "description": " Each pair 'key:value' is treated as 'field:value-to-select'. Remove from the table all rows which contain the selected value in the selected field. The values are considered to be strings, so, for example 0 != 0.0",
                            "additionalProperties": {
                                "type": "string"
                            },
                        },
                        "numerical_range_remove": {
                            "type": "object",
                            "description": "Each key identifies a field. Its value specifies the minimum and maximum values allowed for that field. Remove from the table all rows which have the selected field between the min_value and max_value selected. Min and max are not removed from the table and the values in the field must be numerical.",
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "min_value": {
                                        "type": "number",
                                    },
                                    "max_value": {
                                        "type": "number",
                                    },
                                },
                                "required": ["min_value", "max_value"],
                                "additionalProperties": False
                            }
                        },
                        "alphabetical_range_remove": {
                            "type": "object",
                            "description": "Each key identifies a field. Its value specifies the minimum and maximum values allowed for that field. Remove from the table all rows which have the selected field alphabetically between the min_value and max_value selected. Min and max are not removed from the table.",
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "min_value": {
                                        "type": "string",
                                    },
                                    "max_value": {
                                        "type": "string",
                                    },
                                },
                                "required": ["min_value", "max_value"],
                                "additionalProperties": False
                            }
                        },
                    },
                    "additionalProperties": False,
                },
            },
            "required": ["target_table", "filters"],
            "additionalProperties": False,
        },
    },
}
