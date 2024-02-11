from pathlib import Path

root_dir = Path("Files")

for path in root_dir.rglob("*.csv"):
    if path.is_file():
        new_filepath = path.with_suffix(".txt")
        path.rename(new_filepath)