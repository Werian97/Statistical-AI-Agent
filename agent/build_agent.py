import os
import argparse
import json
from typing import cast

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletion, ChatCompletionMessageFunctionToolCall
from argparse import Namespace

from dotenv import load_dotenv
from agent.tools.call_functions import call_function

from agent.prompts import system_prompt
from agent.tools.call_functions import available_functions

def call_client() -> OpenAI:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("Openrouter API key not found")

    client: OpenAI = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    return client

def read_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="Statistical AI Agent",
        description="take a question from CLI about a CSV file and try to answer it"
    )
    parser.add_argument("user_prompt", type=str, help="this is the user prompt")
    parser.add_argument("--verbose", action="store_true", help="enable verbose output")
    return parser.parse_args()

def ask_question(client: OpenAI, args: Namespace) -> ChatCompletion:
    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": args.user_prompt,},
        {"role": "system", "content": system_prompt}
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions
    )
    return response

def print_response(response: ChatCompletion, args: Namespace):
    if response.usage is None:
        raise RuntimeError("response failed")

    message = response.choices[0].message
    cast(ChatCompletionMessageParam, message)
    if message.tool_calls is not None:
        for tool_call in message.tool_calls:
            if isinstance(tool_call, ChatCompletionMessageFunctionToolCall):
                function_args = json.loads(tool_call.function.arguments or "{}")
                print(f"Calling function: {tool_call.function.name}({function_args})")
                result_message: dict = call_function(tool_call, args.verbose)
                if args.verbose:
                    print(f"-> {result_message['content']}")
            else:
                print("Something unexpected happened")
    else:
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        print(response.choices[0].message.content)