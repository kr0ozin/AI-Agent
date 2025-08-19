import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test_get_files_info():
    test_cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../")
    ]

    for working_dir, directory in test_cases:
        if directory == ".":
            dir = "current"
        else:
            dir = directory
        result = f"Result for {dir} directory:\n{get_files_info(working_dir, directory)}\n"
        print(result)

def test_get_file_content():
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for working_dir, file_path in test_cases:
        print(get_file_content(working_dir, file_path))

if __name__ == "__main__":
    #test_get_files_info()
    test_get_file_content()