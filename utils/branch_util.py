import os


def resolve_branch():
    branch_name = open('./.shit/HEAD').read()
    last_commit = open(os.path.join('./.shit/refs/', branch_name)).read().strip()
    return last_commit, branch_name


def update_branch_commit(commit_hash):
    branch_name = open('./.shit/HEAD').read()
    with open(os.path.join('./.shit/refs/', branch_name), 'w') as f:
        f.write(commit_hash)
