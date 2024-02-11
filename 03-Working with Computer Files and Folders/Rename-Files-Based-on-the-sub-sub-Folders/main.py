from pathlib import Path

root_dir = Path('Files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        path_parts = path.parts
        subFolders = path.parts[1:-1]
        new_filename = '-'.join(subFolders) + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
