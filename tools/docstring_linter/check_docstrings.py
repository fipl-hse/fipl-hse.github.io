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

    all_errors = []

    for lab_name in labs_list:
        lab_errors = ''
        lab_path = project_root_path.joinpath(lab_name)
        main_path = lab_path.joinpath('main.py')

        print(f'\nChecking {main_path}')
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
            lab_errors += f'Darglint errors:\n{result.stdout}'

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
            lab_errors += f'Pydocstyle errors:\n{result.stdout}'

        if lab_errors:
            all_errors.append(f'\nDocstrings in {main_path} do not conform to Google-style.\n'
                              f'ERRORS:\n{lab_errors}\n')

    if all_errors:
        print('\n'.join(all_errors))
        print(f'\nThe docstring check was not successful! Check the logs above.')

        log_file_path = PROJECT_ROOT.joinpath('docstring_check.log')
        with open(file=log_file_path, mode='w', encoding='utf-8') as log_file:
            log_file.write('\n'.join(all_errors))
        print(f'Full check log could be found in: {log_file_path}.\n')

        print('The error explanations for\n'
              'Darglint: https://github.com/terrencepreilly/darglint#error-codes\n'
              'Pydocstyle: http://www.pydocstyle.org/en/stable/error_codes.html')
    exit(bool(all_errors))


if __name__ == '__main__':
    check_docstrings(project_root_path=PROJECT_ROOT,
                     labs_list=PROJECT_CONFIG.get_labs_names())
