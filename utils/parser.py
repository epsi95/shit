import os.path
import sys
from .create_empty_repo import create_empty_repo
from .print_logo import print_logo
from .add_files_to_staging_area import add_files_to_staging_area
from .show_status import show_status
from .commit_util import commit
from .log_util import log
from .reset_util import reset


def get_arg(index):
    try:
        return sys.argv[index]
    except IndexError:
        return None


def check_shit_repo_exist():
    if not os.path.exists('./.shit'):
        print('shit repo does not exist. Please create one with - shit init')
        exit()


if get_arg(1) is None:
    print_logo()
elif get_arg(1) == 'init':
    print('Initializing empty shit repository here')
    create_empty_repo()
elif get_arg(1) == 'add':
    check_shit_repo_exist()
    if get_arg(2) is None:
        print('Invalid arguments. shit add <path>')
    else:
        add_files_to_staging_area(get_arg(2))
elif get_arg(1) == 'status':
    check_shit_repo_exist()
    show_status()
elif get_arg(1) == 'commit':
    check_shit_repo_exist()
    if get_arg(2) is None:
        print('Invalid arguments. shit commit <message>')
    else:
        commit(get_arg(2))
elif get_arg(1) == 'log':
    check_shit_repo_exist()
    log()
elif get_arg(1) == 'reset':
    check_shit_repo_exist()
    if get_arg(2) is None:
        print('Invalid arguments. shit reset <commit-hash>')
    else:
        reset(get_arg(2))
