import os
import zipfile

zip_file_name = "./backup/my_archive.zip"
source_dir = "./db"

with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as zip_object:
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zip_object.write(file_path, os.path.relpath(file_path, source_dir))