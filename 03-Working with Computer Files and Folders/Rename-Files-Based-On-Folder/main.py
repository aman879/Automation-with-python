from pathlib import Path

root_dir = Path('Files')
# file_paths = root_dir.iterdir()

# for path in file_paths:
#     for filepath in path.iterdir():
#         print(filepath)
#             OR

file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + "-" + path.name
        new_pathname = path.with_name(new_filename)
        path.rename(new_pathname)