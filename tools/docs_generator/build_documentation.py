import os
import shutil
import subprocess
from pathlib import Path

from config.constants import (DOC_BUILD_DIR,
                              WEBSITE_ROOT)
from tools.helpers import prepare_args_for_shell


def build_documentation(build_directory: Path) -> None:
    # TODO: Currently assumes only one repository -> one version
    # TODO: make use of sphinx-versioned and refactor
    """Build full website from sources

    Args:
        build_directory:

    Returns:

    """
    print(f'Clearing docs build directory: {build_directory}')
    shutil.rmtree(path=build_directory, ignore_errors=True)

    os.makedirs(name=build_directory,
                exist_ok=True)

    print(f'Building documentation...')
    args = [
        'sphinx-build',
        '-b',
        'html',
        WEBSITE_ROOT,
        build_directory
    ]
    args = prepare_args_for_shell(args)
    print(f'HTML BUILD COMMAND: {args}')
    result_html = subprocess.run(args=args,
                                 text=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 shell=True)
    if result_html.returncode != 0:
        print(f'There are problems with building html: {result_html.stdout}')

    args = [
        'sphinx-build',
        '-b',
        'docx',
        WEBSITE_ROOT,
        build_directory
    ]
    args = prepare_args_for_shell(args)
    print(f'DOCX BUILD COMMAND: {args}')
    result_docs = subprocess.run(args=args,
                                 text=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 shell=True)
    if result_docs.returncode != 0:
        print(f'There are problems with building docx: {result_docs.stdout}')

    if not result_html.returncode and not result_docs.returncode:
        print(f'Documentation is built in {build_directory}')

        full_build_log = 'BUILD LOG:\n' + result_html.stdout + '\n' + result_docs.stdout
        log_file_path = build_directory.joinpath('build.log')
        with open(file=log_file_path, mode='w', encoding='utf-8') as log_file:
            log_file.write(full_build_log)

        print(f'Full build log could be found in: {log_file_path}. Do not forget to check for warnings!')


if __name__ == '__main__':
    build_documentation(build_directory=DOC_BUILD_DIR)
