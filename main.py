import argparse
import os
from dotenv import load_dotenv
import agent

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY key not found in .env")

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("-d_no_agent", action='store_true', help="Debug non agent code by not sending API requests.")
    parser.add_argument("user_prompt", type=str, help="User prompt sent to API gateway")
    args = parser.parse_args() # Now we can access `args.user_prompt`

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    print(f'User prompt: {args.user_prompt}')
    try:
        response = agent.request(api_key, messages, args.d_no_agent)
        print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n')
        print(f'openrouter repsonse: {response.choices[0].message.content}\n')

    except Exception as e:
        response = None
        print(f'Error returned by our agent: {e}')


if __name__ == "__main__":
    main()
