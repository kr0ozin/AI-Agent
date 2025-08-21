import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

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

def test_write_file():
    test_cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this hsould not be allowed")
    ]

    for working_dir, file_path, content in test_cases:
        print(write_file(working_dir, file_path, content))

def test_run_python():
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py")
    ]

    for working_dir, file_path, *extra_args in test_cases:
        args = extra_args[0] if extra_args else []
        print(run_python_file(working_dir, file_path, args))

if __name__ == "__main__":
    #test_get_files_info()
    #test_get_file_content()
    #test_write_file()
    test_run_python()