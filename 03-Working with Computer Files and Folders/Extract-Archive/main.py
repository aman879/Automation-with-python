from pathlib import Path
import zipfile

archive_dir = Path('Archived Files')
destination_dir = Path('destination')

for path in archive_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_dir / Path(path.stem)
        zf.extractall(path=final_path)