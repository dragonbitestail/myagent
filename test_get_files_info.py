from functions.get_files_info import get_files_info

for test_dir in [".", "pkg", "/bin", "../"]:
    print("Result for current directory:")
    print(get_files_info("calculator", test_dir))
