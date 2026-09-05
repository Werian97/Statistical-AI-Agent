from typing import cast

from agent import build_agent

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam, ChatCompletionMessageFunctionToolCall
from argparse import Namespace

from data.read_write_data import clean_temporary

from agent.prompts import system_prompt
from agent.agent_settings import MAX_ITERATION

def main():
    client: OpenAI = build_agent.call_client()
    args: Namespace = build_agent.read_arguments()

    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": args.user_prompt,},
        {"role": "system", "content": system_prompt}
    ]
    response: ChatCompletion
    for _ in range(MAX_ITERATION):
        response = build_agent.ask_question(client, messages)
        tool_calls = cast(None | list[ChatCompletionMessageFunctionToolCall], response.choices[0].message.tool_calls)
        if tool_calls is None:
            break
        build_agent.handle_tool_call(tool_calls, args, messages) #updates messages
    if response.choices[0].message.tool_calls is not None:
        print(f"The AI agent couldn't answer in {MAX_ITERATION} iterations")
        clean_temporary()
        exit(1)
    build_agent.print_response(response, args)

    clean_temporary()
    return

main()
