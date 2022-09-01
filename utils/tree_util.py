import os.path

from .create_hash import create_hash
import json
import shutil


def create_blob(file, hash_, type_data):
    if not os.path.exists(os.path.join('./.shit/objects/', hash_)):
        os.mkdir(os.path.join('./.shit/objects/', hash_), mode=644)
        with open(os.path.join('./.shit/objects/', hash_, 'type.json'), 'w') as f:
            f.write(json.dumps(type_data))
        if file:
            shutil.copy(file, os.path.join('./.shit/objects/', hash_))


def create_tree(files):
    base_tree = {
        'children': []
    }
    for each_file in files:
        data = open(each_file, 'rb').read()
        hash_ = create_hash(data)
        create_blob(each_file, hash_, {
            'type': 'file'
        })
        base_tree['children'].append({
            'path': each_file,
            'hash': hash_
        })
    with open('./.shit/stage_tree.json', 'w') as f:
        json.dump(base_tree, f)


def read_tree():
    return json.loads(open('./.shit/stage_tree.json').read()) if os.path.exists('./.shit/stage_tree.json') else {
        'children': []
    }


def dump_tree():
    data = open('./.shit/stage_tree.json', 'rb').read()
    hash_ = create_hash(data)
    create_blob('./.shit/stage_tree.json', hash_, {
        'type': 'tree'
    })
    return hash_
