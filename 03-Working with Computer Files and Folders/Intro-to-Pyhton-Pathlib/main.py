# ----------------------------------------
# Methods 1
# ----------------------------------------

# p1 = 'Files/abc.txt'

# with open(p1, 'r') as file:
#     print(file.read())

# ------------------------------------------
# Methods 2
# ------------------------------------------

from pathlib import Path

p1 = Path('Files/abc.txt')
print(p1)

if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

p2 = Path('Files/ghi.txt')

if not p2.exists():
    with open(p2, 'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem)
print(p1.suffix)

p3 = Path('Files')
print(p3.iterdir())
print(list(p3.iterdir()))
for item in p3.iterdir():
    print(item)
    with open(item, 'r') as file:
        print(file.read())