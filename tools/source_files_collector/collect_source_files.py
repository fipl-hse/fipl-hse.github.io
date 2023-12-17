"""

"""
import os
import shutil
import subprocess
from pathlib import Path

from tools.helpers import prepare_args_for_shell
from tools.source_files_collector.argument_parser import parser


def get_files_to_collect_from_file(files_to_collect_path: Path) -> list[Path]:
    with open(file=files_to_collect_path, encoding='utf-8', mode='r') as fd:
        files_to_collect = map(Path, fd.read().split('\n'))
        return list(files_to_collect)


def collect_source_files_from_repo(repository: str,
                                   destination: Path) -> None:
    """
    Expects the repository to have a BOM file under config/website/bom.txt

    Args:
        repository:
        destination: an absolute path in which the repository will be sparsely cloned

    Returns:

    """

    # Purge destination directory
    if os.path.isdir(destination):
        shutil.rmtree(path=destination)

    # Sparsely checkout repository
    # Requires git v2.37.1+
    clone_args = [
        'git',
        'clone',
        '--no-checkout',
        '--depth',
        '1',
        '--filter=blob:none',
        '--sparse',
        repository,
        destination
    ]
    clone_args = prepare_args_for_shell(clone_args)
    print(f'Collecting repository: {repository} with: {clone_args}')
    subprocess.run(args=clone_args,
                   shell=True)

    # Checkout config to get files to collect
    # NOTE: Requires a leading slash
    bom_path = '/config/website/bom.txt'

    # Set the BOM file for checkout
    checkout_args = [
        'git',
        'sparse-checkout',
        'set',
        '--no-cone',
        bom_path
    ]
    checkout_args = prepare_args_for_shell(checkout_args)
    print(f'Checking out BOM...')
    subprocess.run(args=checkout_args,
                   shell=True,
                   cwd=destination)
    checkout_args = [
        'git',
        'checkout'
    ]
    subprocess.run(args=prepare_args_for_shell(checkout_args),
                   shell=True,
                   cwd=destination)

    # Set the required files for checkout
    files_to_collect = get_files_to_collect_from_file(destination.joinpath(bom_path))
    checkout_args = [
        'git',
        'sparse-checkout',
        'set',
        '--no-cone',
        prepare_args_for_shell(files_to_collect)
    ]
    checkout_args = prepare_args_for_shell(checkout_args)
    print(f'Setting files to checkout with: {checkout_args}')
    subprocess.run(args=checkout_args,
                   shell=True,
                   cwd=destination)
    # Checkout files
    checkout_args = [
        'git',
        'checkout'
    ]
    subprocess.run(args=prepare_args_for_shell(checkout_args),
                   shell=True,
                   cwd=destination)

    # Remove git tree/objects
    shutil.rmtree(destination.joinpath('.git'), ignore_errors=True)
    # Remove config
    shutil.rmtree(destination.joinpath('config'), ignore_errors=True)


if __name__ == '__main__':
    # TODO: Currently works only with one repository

    # Example usage:
    # python collect_source_files.py \
    # --repository https://github.com/org/repository.git \
    # --destination ../../labs
    args = parser.parse_args()

    collect_source_files_from_repo(repository=args.repository,
                                   destination=args.destination)
