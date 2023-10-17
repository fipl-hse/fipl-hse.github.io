import subprocess
from pathlib import Path

from config.constants import (PROJECT_ROOT,
                              API_DOC_TEMPLATES_PATH,
                              RST_DOCS_ROOT,
                              PROJECT_CONFIG)


def generate_api_docs(project_root_path: Path,
                      labs_list: list[str],
                      rst_docs_root: Path,
                      apidoc_templates_path: Path,
                      overwrite: bool = False) -> None:
    """Generate API docs for all laboratory works.

    Iterate over all the lab* folders under the project_root_path and
    generate the API .rst document in the corresponding folder under the
    rst_docs_root/lab_name.

    Args:
        project_root_path:
        labs_list:
        rst_docs_root:
        apidoc_templates_path:
        overwrite:

    Returns:

    """

    for lab_name in labs_list:
        lab_path = project_root_path.joinpath(lab_name)
        lab_doc_api_path = rst_docs_root.joinpath(lab_name)

        args = [
            'sphinx-apidoc',
            '-o',
            lab_doc_api_path,
            '--no-toc',
            '--no-headings',
            '--suffix',
            'api.rst',
            '-t',
            apidoc_templates_path,
            lab_path
        ]
        if overwrite:
            args.insert(-1, '-f')

        excluded_paths = (lab_path.joinpath('tests'), lab_path.joinpath('assets'), lab_path.joinpath('start.py'))
        args.extend(excluded_paths)

        print(f'FULL COMMAND: {" ".join(map(str, args))}')
        result = subprocess.run(args=args)
        if result.returncode == 0:
            print(f'API DOC FOR {lab_path} GENERATED IN {lab_doc_api_path}\n')
        else:
            print(f'ERROR WITH CODE: {result.returncode} + {result.stderr}\n')


if __name__ == '__main__':

    generate_api_docs(project_root_path=PROJECT_ROOT,
                      labs_list=PROJECT_CONFIG.get_labs_names(),
                      rst_docs_root=RST_DOCS_ROOT,
                      apidoc_templates_path=API_DOC_TEMPLATES_PATH,
                      overwrite=True)
