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
    parser.add_argument("--d_no_agent", action='store_true', help="Debug non agent code by not sending API requests.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt sent to API gateway")
    args = parser.parse_args() # Now we can access `args.user_prompt`

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    try:
        response = agent.request(api_key, messages, args)
    except Exception as e:
        response = None
        print(f'Error returned by our agent: {e}')


if __name__ == "__main__":
    main()
