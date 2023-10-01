import os
from pathlib import Path


def path_to_file(file_name: str) -> str:
    print(Path(Path.cwd().parents[2]))
    for root, dirs, files in os.walk(Path(Path.cwd().parents[2])):
        for name in files:
            if name == file_name:
                return os.path.abspath(os.path.join(root, name))
    raise Exception(f'file {file_name} doesnt found in project directory')
