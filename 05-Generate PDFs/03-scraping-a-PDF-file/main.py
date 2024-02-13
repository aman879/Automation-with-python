import fitz
from pathlib import Path

root_dir = Path(".")
filename = "pdfScarapper" + ".txt"
filepath = root_dir / Path(filename)

with fitz.open("students.pdf") as pdf:
    text = ''
    for page in pdf:
        text = text + page.get_text()

with open(filename, 'w') as file:
    file.write(text)