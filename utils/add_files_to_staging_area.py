import os
from .tree_util import create_tree


def add_files_to_staging_area(path):
    files_to_be_staged = []
    if path.strip() == '.':
        for root, dirs, files in os.walk('./'):
            dirs[:] = [d for d in dirs if d not in '.shit/']
            for file in files:
                files_to_be_staged.append(os.path.join(root, file))
    else:
        files_to_be_staged = [path]

    create_tree(files_to_be_staged)
