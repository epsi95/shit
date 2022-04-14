import sys
from .create_empty_repo import create_empty_repo
from .print_logo import print_logo
from .add_files_to_dtaging_area import add_files_to_staging_area


def get_arg(index):
    try:
        return sys.argv[index]
    except IndexError:
        return None


if get_arg(1) is None:
    print_logo()
elif get_arg(1) == 'init':
    print('Initializing empty shit repository here')
    create_empty_repo()
elif get_arg(1) == 'add':
    if get_arg(2) is None:
        print('Invalid arguments')
    else:
        add_files_to_staging_area(get_arg(2))
