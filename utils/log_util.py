from .branch_util import resolve_branch
from .commit_util import get_all_commits


def log():
    last_commit, branch_name = resolve_branch()
    if not last_commit:
        exit()
    current_commit = tail_commit = get_all_commits()
    while current_commit:
        print(f'● {current_commit.hash_[-4:]}  {current_commit.message}')
        print('|')
        current_commit = current_commit.prev

