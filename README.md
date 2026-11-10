
# myagent

A basic, AI agent which interacts with [openai router](https://openrouter.ai/).

# Background

Implementation of Boot.Dev course: Build an AI Agent in Python.

# WARNING

This is a test project by an amateur hobbyist with very limited experience in 
AI.  As guided by the course, attempts were made to limit this AI agent's
access to files outside the working directory's sample calculator app
sub-directory of this agent but, caution should still be exercised when running
this code.

For example, one of the tools the agent can run is the ability to write files
and no safe-guard currently exists for overwriting existing files.

In addition to the limits imposed on the agent in code, my development
environment limits access by running the agent inside a virtual machine.

If you plan on removing the current limitations, in order to increase the
usefulness of the agent then it would behoove you to enact a model which limits
file access in some manner such as using a VM.

# Install

## Prerequisites

* Python 3.14+
* An account and API key from [openai router](https://openrouter.ai/).
    All testing was done using their free account.

*TODO* for now just a brief summary

* Clone the code locally and cd to the project directory.
* Install uv or a comparable Python environment manager. E.g.  Python Virtual
  environment.
* Within your Python environment for your project install: `openai` and python-dotenv Python
  packages.

# Run

With your Python environment active:
`python main.py  "What can you do?"`

or, using `uv`:

`uv run main.py  "What can you do?"`

OUTPUT:
```
openrouter repsonse: I can assist with various tasks involving file management and Python scripting. Here's what I can do:

1. **List Files/Directories**: Retrieve information about files (size, type) or directories in a specified folder.
2. **Read File Contents**: Extract and view the content of a specific file.
3. **Run Python Scripts**: Execute Python files with optional arguments for automation or data processing.
4. **Write/Overwrite Files**: Create or modify files by inputting new content.

For example, I can help you:
- Check the structure of a project directory.
- Debug a Python script by running it with specific arguments.
- Modify configuration files or generate new data files.

Let me know how I can assist you with a specific task!
```
