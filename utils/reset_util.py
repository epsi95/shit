import os
import shutil

from .commit_util import get_all_commits


def reset(commit_hash):
    commit = get_all_commits()
    my_commit_obj = None
    while commit:
        if commit.hash_.endswith(commit_hash):
            my_commit_obj = commit
            break
        commit = commit.prev

    if not my_commit_obj:
        print(f'no valid commit found with {commit_hash}')
        return

    for item in os.listdir(os.getcwd()):
        if item not in ['.shit']:
            if os.path.isdir(item):
                shutil.rmtree(item)
                continue
            os.remove(item)

    for each_blob in my_commit_obj.child.children:
        each_blob.restore()
