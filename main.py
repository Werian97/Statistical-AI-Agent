from agent import build_agent

from openai import OpenAI
from openai.types.chat import ChatCompletion
from argparse import Namespace

def main():
    client: OpenAI = build_agent.call_client()
    args: Namespace = build_agent.read_arguments()

    response: ChatCompletion = build_agent.ask_question(client, args)
    build_agent.print_response(response, args)

main()