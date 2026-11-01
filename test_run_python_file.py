from functions.run_python_file import run_python_file

tests = [
    ["calculator", "main.py", []],
    ["calculator", "main.py", ["3 + 5"]],
    ["calculator", "tests.py", []],
    ["calculator", "../main.py", []],
    ["calculator", "nonexistent.py", []],
    ["calculator", "lorem.txt", []],
]
for tt in tests:
    print(run_python_file(tt[0], tt[1], tt[2]))
