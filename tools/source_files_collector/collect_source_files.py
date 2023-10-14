"""

"""

import subprocess
from pathlib import Path
import shutil

from tools.helpers import prepare_args_for_shell


def collect_source_files(repository: str,
                         files_to_collect: tuple[Path],
                         destination: Path) -> None:
    """

    Args:
        repository:
        files_to_collect:
        destination:

    Returns:

    """

    # Sparsely checkout repository
    clone_args = [
        'git',
        'clone',
        '-n',
        repository,
        '--depth',
        '1',
        destination
    ]
    clone_args = prepare_args_for_shell(clone_args)
    subprocess.run(args=clone_args,
                   shell=True)

    # Checkout the latest versions of the required files
    for file_to_collect in files_to_collect:
        checkout_args = [
            'git',
            'checkout',
            'HEAD',
            file_to_collect
        ]
        checkout_args = prepare_args_for_shell(checkout_args)

        print(f'Collecting {file_to_collect} with: {checkout_args}')
        subprocess.run(args=checkout_args,
                       shell=True,
                       cwd=destination)

    # Remove git tree
    shutil.rmtree(destination.joinpath('.git'))
