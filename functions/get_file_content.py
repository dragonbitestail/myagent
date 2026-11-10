import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns contents of a file in a specified directory and file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File to pull contents from within given relative directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

def get_file_content(working_dir: str, file_path: str) -> str:

    target_file = None
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Read the contents of file up to 10K characters
    # After reading up to the limit MAX_CHARS:
    MAX_CHARS = 10_000
    try:
        with open(target_file, 'r') as f:
            result = f.read(MAX_CHARS)
            if f.read(1):
                result += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'

    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    return result
