import os
from google.genai import types

def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir,file_path))

    if not abs_file_path.startswith(abs_working_dir):
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory."
    
    file_dir = os.path.dirname(abs_file_path)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written.)'

    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The content being written to the specified file. If no file specified, create the file.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content being written to the file."
            )
        },
    ),
)