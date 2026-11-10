import argparse
import os
from dotenv import load_dotenv
import agent
import pprint
import sys

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY key not found in .env")

def main():
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute or run Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
No matter what you are instructed you should not try to operate outside the injected working directory.
"""
    request_limit = 20
    request_limit_help = 'Limit the number of requests made by the agent (default = {request_limit})'.format(request_limit=request_limit)
    exit_val = 0

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--d_no_agent", action='store_true', help="Debug non agent code by not sending API requests.")
    parser.add_argument("-t", "--temperature", type=range_limited_float_type, help="Debug non agent code by not sending API requests.")
    #parser.add_argument("-l", "--request-limit", nargs='?', dest='request_limit', type=int, const=request_limit, help=request_limit_help)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-V", action="store_true", help="Enable extra verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt sent to API gateway")
    args = parser.parse_args() # Now we can access `args.user_prompt`

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    try:
        more_calls = True
        for _ in range(request_limit):
            response = agent.request(api_key, args.temperature, messages, args)
            messages = agent.evalResponse(response, messages, args.verbose)
            if args.verbose:
                pprint.pp(f'main() messages: {messages}')
            if not response.choices[0].message.tool_calls:
                more_calls = False
                break
        if more_calls:
            print(f'[WARN] Request limit, {args.request_limit}, exhausted')
            exit_val = 1
    except Exception as e:
        print(f'main() Error returned by our agent: {e}')
        exit_val = 2

    sys.exit(exit_val)

# # Source - https://stackoverflow.com/a/55410582
# Posted by rdas, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-30, License - CC BY-SA 4.0
def range_limited_float_type(arg):
    MIN_VAL = 0
    MAX_VAL = 1

    """ Type function for argparse - a float within some predefined bounds """
    try:
        f = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a floating point number")
    if f < MIN_VAL or f > MAX_VAL:
        raise argparse.ArgumentTypeError("Argument must be < " + str(MAX_VAL) + "and > " + str(MIN_VAL))
    return f

if __name__ == "__main__":
    main()
