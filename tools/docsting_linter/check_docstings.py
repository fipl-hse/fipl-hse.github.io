"""
Check docstrings for conformance to the Google-style-docstrings

Darglint tool is used for docstring completion check,
i.e., all parameters are present and have typings, etc.

Pydocstyle is used for docstring style check,
i.e., all new lines are present, correct wording & punctuation, etc.
"""
from pathlib import Path


def check_docstrings(project_root_path: Path,
                     labs_list: list[str]) -> None:
    pass
