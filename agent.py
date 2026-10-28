from openai import OpenAI

def request(api_key, messages, args):
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
        )

    if response is None:
        raise Exception("Skipped API request. debug_skip_api is true.")
    elif response.usage is None:
        raise RuntimeError("No usage data. Possible API failure")

    if args.verbose:
        print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\n')

    print(f'openrouter repsonse: {response.choices[0].message.content}\n')

    return response
