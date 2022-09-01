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
    with open('./.shit/refs/main', 'w') as f:
        f.write('')
    # creating some additional files
    with open('./.shit/HEAD', 'w') as f:
        f.write('main')
