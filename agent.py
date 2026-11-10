from openai import OpenAI
from call_function import available_functions
from call_function import call_function
import json
import pprint

# use None for temp to get a models default temperature
def request(api_key, temp, messages, args):
    response = None

    if args.verbose:
        print(f'User prompt: "{args.user_prompt}"')

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
        #raise Exception("Skipped API request. debug_skip_api is true.")
        response = "No response. d_no_agent is true?"
        #response = I don't know how to create a dummy response.....
    elif response.usage is None:
        raise RuntimeError("No usage data. Possible API failure")

    if args.verbose:
        print(f'Selected Model: {response.model}\n')
        print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n')


    if args.V:
        pprint.pp(f'request(): return: {response} of type: {type(response)}')
    return response

def evalResponse(response: ChatCompletionResponse, messages, verbose: bool):
    # response should only be str type when using skip agent command-line flag.
    if isinstance(response, str):
        messages.append(response)
        return messages

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls is not None:
        tResults = call_function(message.tool_calls[0], verbose)
        if tResults["content"] == "":
            raise RuntimeError("evalResponse() Empty content found in results")
        if verbose:
            print(f"-> {tResults["content"]}")
        messages.append(tResults)
        print(f'assistant: {tResults["content"]}')
    else:
        print(f'openrouter repsonse: {response.choices[0].message.content}\n')

    return messages
