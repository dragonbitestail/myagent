from openai import OpenAI
from call_function import available_functions
import json

# use None for temp to get a models default temperature
def request(api_key, temp, messages, args):
    response = None

    if args.verbose:
        print(f'User prompt: {args.user_prompt}')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    if not args.d_no_agent:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=temp,
            tools=available_functions,
        )

    if response is None:
        raise Exception("Skipped API request. debug_skip_api is true.")
    elif response.usage is None:
        raise RuntimeError("No usage data. Possible API failure")

    if args.verbose:
        print(f'Selected Model: {response.model}\n')
        print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n')

    return response

def evalResponse(response: ChatCompletionResponse):
    message = response.choices[0].message

    if message.tool_calls is not None:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(f'openrouter repsonse: {response.choices[0].message.content}\n')
