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

def ask_question(client: OpenAI, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions
    )
    messages.append(cast(ChatCompletionMessageParam, response.choices[0].message))

    if response.usage is None:
        raise RuntimeError("response failed")
    
    return response

def handle_tool_call(tool_calls: list[ChatCompletionMessageFunctionToolCall], args: Namespace, messages: list[ChatCompletionMessageParam]):
    for tool_call in tool_calls:
        if isinstance(tool_call, ChatCompletionMessageFunctionToolCall):
            result_message: ChatCompletionMessageParam = call_function(tool_call, args.verbose)
            messages.append(result_message)
        else:
            raise Exception("tool_call is expected to be an instance of 'ChatCompletionMessageFunctionToolCall'")

def print_response(response: ChatCompletion, args: Namespace):
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage is not None:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)