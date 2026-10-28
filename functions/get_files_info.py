import os

def get_files_info(working_dir: str, directory: str = ".") -> str:
    target_dir = None
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: encountered underlying raised exception {e}'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    #print(f'DEBUG: building file info from target_dir {target_dir}\n')
    files_info_out = []
    for file in os.listdir(target_dir):
        full_path = os.path.join(target_dir, file)
        #print(f"item: {file}")
        file_info = [f'- {file}:']
        try:
            file_info.append(f'file_size={os.path.getsize(full_path)}')
            if os.path.isdir(full_path):
                file_info.append(f'is_dir=True')
            else:
                file_info.append(f'is_dir=False')

            files_info_out.append(', '.join(file_info))
        except Exception as e:
            return f'Error: encountered underlying raised exception {e}'

    return "\n".join(files_info_out)
