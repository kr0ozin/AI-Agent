import os

def get_files_info(working_dir, directory="."):
    try: 
        working_dir = os.path.join(os.getcwd(), working_dir)
        directory = os.path.join(working_dir, directory)
        
        if os.path.abspath(working_dir) not in os.path.abspath(directory):
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory."
        if not os.path.isdir(directory):
            return f"Error: '{directory}' is not a directory."
        
        full_path = os.path.join(working_dir, directory)

        path_contents = os.listdir(full_path)
        files_info = []

        for file in path_contents:
            file_path = os.path.join(full_path, file)
            file_info = {
                "name": file,
                "size": os.path.getsize(file_path),
                "is_directory": os.path.isdir(file_path),
            }
            result = f"- {str(file_info['name'])}: file_size={str(file_info['size'])}, is_dir={str(file_info['is_directory'])}"
            files_info.append(result)

    except Exception as e:
        return f"Error: {str(e)}"


    return "\n".join(files_info)
