from pathlib import Path
import zipfile

root_dir = Path('Files')
archived_files_dir = Path('Archived Files') 
archive_path = archived_files_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink()