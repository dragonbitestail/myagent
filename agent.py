from openai import OpenAI

def request(api_key, messages, debug_skip_api):
    response = None

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    if not debug_skip_api:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
        )

    if response is None:
        raise Exception("Skipped API request. debug_skip_api is true.")
    elif response.usage is None:
        raise RuntimeError("No usage data. Possible API failure")

    return response
