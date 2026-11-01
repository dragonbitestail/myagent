from functions.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")
#print(f"lorem.txt : {result}")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

for test_file in ["main.py", "pkg/calculator.py", "/bin/cat",
                 "pkg/does_not_exist.py"]:
    print(get_file_content("calculator", test_file))
