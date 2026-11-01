import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a Python file with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File to run as a Python script within relative directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Optional arguments to add to the Python file being run",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_dir: str, file_path: str,
    args: list[str] | None = None
) -> str:

    target_file = None
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    # target_file meets all criteria. Attempt to execute it:
    command = ["python", target_file]
    if args is not None and len(args) > 0:
        command.extend(args)

    process_results_str = None
    try:
        script_dir = os.path.dirname(target_file)
        process_out = subprocess.run(command, cwd=script_dir, capture_output=True, text=True, timeout=30)

        process_results_str = buildProcessOutStr(process_out)
    except Exception as e:
        return f"Error: executing Python file: {e}"


    return process_results_str

def buildProcessOutStr(process_o: subprocess.CompletedProcess) -> str:
    out_str = ""

    try:
        if process_o.returncode != 0:
            out_str += "Process exited with code X"
        if ((process_o.stdout is None or process_o.stdout == "") and
            (process_o.stderr is None or process_o.stderr == "")):
            out_str += "No output produced"

        if process_o.stdout is not None:
            out_str += "STDOUT: " + process_o.stdout
        if process_o.stderr is not None:
            out_str += "STDERR: " + process_o.stderr
    except Exception as e:
        out_str = f"Error: executing Python file: {e}"

    return out_str
