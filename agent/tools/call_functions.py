import json

from openai.types.chat import ChatCompletionToolUnionParam, ChatCompletionMessageParam

from collections.abc import Callable

from agent.tools.get_column_mean import get_column_mean, schema_get_column_mean
from agent.tools.get_fields import get_fields, schema_get_fields
from agent.tools.get_column_max import get_column_max, schema_get_column_max
from agent.tools.get_column_min import get_column_min, schema_get_column_min
from agent.tools.get_column_variance import get_column_variance, schema_get_column_variance
from agent.tools.get_column_covariance import get_column_covariance, schema_get_column_covariance
from agent.tools.get_column_median import get_column_median, schema_get_column_median
from agent.tools.get_column_mode import get_column_mode, schema_get_column_mode

available_functions: list[ChatCompletionToolUnionParam] = [
    schema_get_fields,
    schema_get_column_mean,
    schema_get_column_max,
    schema_get_column_min,
    schema_get_column_variance,
    schema_get_column_covariance,
    schema_get_column_median,
    schema_get_column_mode,
]

function_map: dict[str, Callable[..., str]] = {
    "get_fields": get_fields,
    "get_column_mean": get_column_mean,
    "get_column_max": get_column_max,
    "get_column_min": get_column_min,
    "get_column_variance": get_column_variance,
    "get_column_covariance": get_column_covariance,
    "get_column_median": get_column_median,
    "get_column_mode": get_column_mode,
}

def call_function(tool_call, verbose: bool = False) -> ChatCompletionMessageParam:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    func: Callable | None = function_map.get(function_name)
    if func is None:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }

    content = func(**function_args)
    if verbose:
        print(f"-> {content}")

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": content,
    }