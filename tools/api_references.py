"""
Change API references.
"""
import re
from pathlib import Path

from config.constants import PROJECT_CONFIG_PATH, PROJECT_ROOT, RST_DOCS_ROOT
from config.project_config import ProjectConfig


def update_references(file_paths: list) -> None:
    """
    Change API references to correct ones in lab descriptions.

    Args:
        file_paths (list): Paths to lab description
    """
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        pattern = re.compile(r':py:(class|func|meth):`lab_(.*?)`')
        updated_content = re.sub(pattern, r':py:\1:`stubs.labs_2023.lab_\2`', content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)


if __name__ == '__main__':
    project_config = ProjectConfig(PROJECT_ROOT, PROJECT_CONFIG_PATH)
    labs_list = project_config.get_labs_names()
    rst_files = [file for lab in labs_list
                 for file in Path(RST_DOCS_ROOT / 'labs' / lab).glob('lab[0-9].rst')]
    update_references(rst_files)
