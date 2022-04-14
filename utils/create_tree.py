import os.path

from .create_hash import create_hash
import json
import shutil


def create_blob(file, hash_):
    if not os.path.exists(os.path.join('./.shit/objects/', hash_)):
        os.mkdir(os.path.join('./.shit/objects/', hash_), mode=644)
        shutil.copy(file, os.path.join('./.shit/objects/', hash_))


def create_tree(files):
    base_tree = {
        'files': []
    }
    for each_file in files:
        data = open(each_file, 'rb').read()
        hash_ = create_hash(data)
        create_blob(each_file, hash_)
        base_tree['files'].append({
            'path': each_file,
            'hash': hash_
        })
    with open('./.shit/stage_tree.json', 'w') as f:
        json.dump(base_tree, f)
