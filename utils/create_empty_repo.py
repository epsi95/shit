import os


def create_empty_repo():
    req_folders = [
        './.shit',
        './.shit/objects',
        './.shit/refs',
        './.shit/refs/heads'
    ]
    for each_folder in req_folders:
        os.mkdir(each_folder, mode=644)

    # creating some additional files
    with open('./.shit/HEAD', 'w') as f:
        pass
