import os
import subprocess
from google.genai import types

def run_python_file(working_dir, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir,file_path))

    if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command_to_run = ["python", abs_file_path] + args
        completed_process = subprocess.run(command_to_run, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)
        result = ""
        if completed_process.stdout:
            result += f"STDOUT:\n{completed_process.stdout}"
        if completed_process.stderr:
            result += f'STDERR:\n{completed_process.stderr}'

        if completed_process.returncode != 0:
            result += f"Process exited with code {completed_process.returncode}"
        
        return result if result else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python script, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of python file being called, relative to the working directory.",
            ),
        },
    ),
)