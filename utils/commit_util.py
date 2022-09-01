import json
import os
import glob

from .tree_util import dump_tree, create_blob, create_hash
from .branch_util import resolve_branch, update_branch_commit
from model.commit import Commit
from model.tree import Tree
from model.blob import Blob


def commit(commit_message):
    last_commit_hash = resolve_branch()[0]

    def commit_(prev_commit_hash=None):
        tree_hash = dump_tree()
        commit_blueprint = {
            'type': 'commit',
            'child': tree_hash,
            'message': commit_message,
            'prev_commit_hash': prev_commit_hash
        }
        hash_ = create_hash(json.dumps(commit_blueprint).encode('utf-8'))
        create_blob(None, hash_, commit_blueprint)
        update_branch_commit(hash_)
        print(f'last commit is updated to {hash_[-4:]} for the branch {resolve_branch()[-1]}')

    if last_commit_hash:
        commit_(last_commit_hash)
    else:
        print('creating first commit')
        commit_()


def get_all_commits():
    commits = {}
    for f in glob.glob('./.shit/objects/*/type.json'):
        data = json.loads(open(f).read())
        if data['type'] == 'commit':
            tree = json.loads(open(f'./.shit/objects/{data["child"]}/stage_tree.json').read())
            tree_obj = Tree(data["child"], [Blob(c['hash'], c['path']) for c in tree['children']])
            commit_obj = Commit(os.path.basename(os.path.dirname(f)), data['prev_commit_hash'],
                                tree_obj, data['message'])
            commits[commit_obj.hash_] = commit_obj

    for ec in commits.values():
        if ec.prev:
            ec.prev = commits[ec.prev]

    return commits[resolve_branch()[0]]





