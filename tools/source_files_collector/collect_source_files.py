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


def collect_source_files(repository: str,
                         files_to_collect_path: Path,
                         destination: Path) -> None:
    """

    Args:
        repository:
        files_to_collect_path:
        destination:

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

    files_to_collect = get_files_to_collect_from_file(files_to_collect_path)

    # Set the required files for checkout
    checkout_args = [
        'git',
        'sparse-checkout',
        'add',
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
    shutil.rmtree(destination.joinpath('.git'))

    # `git sparse-checkout` checkouts the top-level files regardless
    # Remove the top-level files that are not in `files_to_collect`
    for file_ in os.listdir(destination):
        if Path(file_) not in files_to_collect:
            destination.joinpath(file_).unlink()


if __name__ == '__main__':
    # Example usage:
    # python collect_source_files.py \
    # --repository "https://github.com/fipl-hse/2023-2-level-labs.git" \
    # --files-to-collect-path ../../config/files_to_collect.txt \
    # --destination ../../labs
    args = parser.parse_args()
    collect_source_files(repository=args.repository,
                         files_to_collect_path=args.files_to_collect_path,
                         destination=args.destination)
