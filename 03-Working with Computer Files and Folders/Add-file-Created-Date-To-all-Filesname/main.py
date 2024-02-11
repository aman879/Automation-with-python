from pathlib import Path
from datetime import datetime



#       GET THE CREATED TIME OF SOME FILE
# stats = path.stat()
# seconds_created = stats.st_ctime
# date_created = datetime.fromtimestamp(seconds_created)
# date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
# print(date_created_str)
def get_time(path):
    stats = path.stat()
    seconds_created = stats.st_ctime
    date_created = datetime.fromtimestamp(seconds_created)
    date_created_str = date_created.strftime("%Y-%m-%d_%H-%M-%S")
    return date_created_str

root_dir = Path('Files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        date_created = get_time(path)
        new_filename = date_created + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)





