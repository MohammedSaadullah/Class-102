import os
import shutil

from_dir = os.path.abspath(os.path.join(os.getenv('USERPROFILE'), 'Downloads'))
to_dir = os.path.abspath(os.path.join(os.getenv('USERPROFILE'), 'Document_Files'))

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    _, file_extension = os.path.splitext(file_name)
    if not file_extension:
        continue

    if file_extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.abspath(os.path.join(from_dir, file_name))
        path2 = to_dir
        path3 = os.path.abspath(os.path.join(to_dir, 'Document_Files', file_name))

        if os.path.exists(path2):
            print(f"Moving {file_name}...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Created folder {path2} and moved {file_name}...")
            shutil.move(path1, path3)
