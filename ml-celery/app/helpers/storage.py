import os
from os import path


def create_path(path_dir):
    if path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)    

def upload_file_bytes(file_bytes, path):
    f = open(path, "wb")
    f.write(file_bytes)
    f.close()
    