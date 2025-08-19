import unittest
from functions.get_files_info import get_files_info

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

if __name__ == "__main__":
    test_get_files_info()