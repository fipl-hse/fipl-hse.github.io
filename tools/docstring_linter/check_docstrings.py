"""
Check docstrings for conformance to the Google-style-docstrings

Google-style-docstrings:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Darglint tool is used for docstring completion check,
i.e., all parameters are present and have typings, etc.

Pydocstyle is used for docstring style check,
i.e., all new lines are present, correct wording & punctuation, etc.
"""
import subprocess
from pathlib import Path

from config.constants import PROJECT_CONFIG, PROJECT_ROOT


def check_docstrings(project_root_path: Path,
                     labs_list: list[str]) -> None:
    """Summary

    Description

    Args:
        project_root_path:
        labs_list:

    Returns:

    """

    has_failed = False

    for lab_name in labs_list:
        all_errors = ''
        lab_path = project_root_path.joinpath(lab_name)
        main_path = lab_path.joinpath('main.py')

        print(f'Checking {main_path}')
        darglint_args = [
            'darglint',
            '--docstring-style',
            'google',
            '--strictness',
            'full',
            '--enable',
            'DAR104',
            main_path
        ]
        print(f'FULL DARGLINT COMMAND: {" ".join(map(str, darglint_args))}')

        result = subprocess.run(args=darglint_args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode == 0:
            print(f'All docstrings in {main_path} conform to Google-style according to Darglint\n')
        else:
            all_errors += f'Darglint errors:\n{result.stdout}'

        pydocstyle_args = [
            'pydocstyle',
            '--convention',
            'google',
            main_path
        ]
        print(f'FULL PYDOCSTYLE COMMAND: {" ".join(map(str, pydocstyle_args))}')

        result = subprocess.run(args=pydocstyle_args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode == 0:
            print(f'All docstrings in {main_path} conform to Google-style according to Pydocstyle\n')
        else:
            all_errors += f'Pydocstyle errors:\n{result.stdout}'

        if all_errors:
            print(f'Docstrings in {main_path} do not conform to Google-style.\n'
                  f'ERRORS:\n{all_errors}\n')
            has_failed = True

    if has_failed:
        print(f'\nThe docstring check was not successful! Check the logs above.')
        print('The error explanations for\n'
              'Darglint: https://github.com/terrencepreilly/darglint#error-codes\n'
              'Pydocstyle: http://www.pydocstyle.org/en/stable/error_codes.html')
    exit(has_failed)


if __name__ == '__main__':

    check_docstrings(project_root_path=PROJECT_ROOT,
                     labs_list=PROJECT_CONFIG.get_labs_names())
