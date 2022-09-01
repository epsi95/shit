import os
from .tree_util import read_tree
from .create_hash import create_hash


def show_status():
    current_snapshot = {}
    for root, dirs, files in os.walk('./'):
        dirs[:] = [d for d in dirs if d not in '.shit/']
        for file in files:
            current_snapshot[os.path.join(root, file)] = create_hash(open(os.path.join(root, file), 'rb').read())

    staged_snapshot = {i['path']: i['hash'] for i in read_tree()['children']}

    name_set_current = set(current_snapshot.keys())
    name_set_staged = set(staged_snapshot.keys())
    name_not_matched = name_set_current.difference(name_set_staged)

    # new file & renamed/moved
    new_files = {nnm: current_snapshot[nnm] for nnm in name_not_matched if
                 current_snapshot[nnm] not in staged_snapshot.values()}
    renamed = {nnm: current_snapshot[nnm] for nnm in name_not_matched if
               current_snapshot[nnm] in staged_snapshot.values()}

    # deleted
    deleted = {f: h for f, h in staged_snapshot.items() if h not in current_snapshot.values()}

    if staged_snapshot:
        print('[staged] :')
        print(*[i + ' ' * (40 - len(i)) + 'hash:' + staged_snapshot[i][-4:] for i in staged_snapshot], sep='\n')
        print('\n')
    if new_files:
        print('[untracked] :')
        print(*[i + ' ' * (40 - len(i)) + 'hash:' + new_files[i][-4:] for i in new_files], sep='\n')
        print('\n')
    if renamed:
        print('[renamed/moved] :')
        print(*[i + ' ' * (40 - len(i)) + 'hash:' + renamed[i][-4:] for i in renamed], sep='\n')
    if deleted:
        print('[modified] :')
        print(*[i + ' ' * (40 - len(i)) + 'hash:' + deleted[i][-4:] for i in deleted], sep='\n')
