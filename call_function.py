import json
from collections.abc import Callable
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]


function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
}

# The three things we care about are:
#  tool_call.function.name: the name of the function (a string)
#  tool_call.function.arguments: the arguments, as a JSON string
#  tool_call.id: a unique ID for this call (we'll need it when we send the result back)
def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    # Why is this not passed as arg...
    function_args["working_dir"] = "./calculator"

    call_msg = f' - Calling function: {function_name}'

    if verbose and len(function_args) > 0:
            call_msg = f'{call_msg}({function_args})'
    print(call_msg)

    # Initialize a results dict assuming error.
    # Otherwise, run the callable and set content to callable's output
    toolResults: dict[str, str] = {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"Error: Unknown function: {function_name}",
    }
    if function_name in function_map:
        toolResults["content"] = function_map[function_name](**function_args)

    return toolResults
