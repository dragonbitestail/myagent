import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY key not found in .env")

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args() # Now we can access `args.user_prompt`

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    print(f'User prompt: {args.user_prompt}')
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if response.usage is None:
        raise RuntimeError("No usage data. Possible API failure")


    print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n')
    print(f'openrouter repsonse: {response.choices[0].message.content}\n')

if __name__ == "__main__":
    main()
