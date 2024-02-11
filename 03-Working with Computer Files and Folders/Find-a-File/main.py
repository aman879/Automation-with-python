from pathlib import Path

root_dir = Path('destination')
search_tem = '14'

for path in root_dir.rglob("*.txt"):
    if path.is_file():
        if search_tem in path.stem:
         print(path.absolute())