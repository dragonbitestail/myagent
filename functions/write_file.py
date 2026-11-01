import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to given file path relative to working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File to write contents to within working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the given file within relative directory",
                },

            },
            "required": ["file_path", "content"],
        },
    },
}

def write_file(working_dir: str, file_path: str, content: str) -> str:

    target_file = None
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    # the contents to file
    try:
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as f:
            #print(f'DEBUG: writing to stream {f}')
            f.write(content)

    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
