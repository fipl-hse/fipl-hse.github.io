from config.project_config import ProjectConfig
from config.constants import PROJECT_CONFIG_PATH, PROJECT_ROOT
from pathlib import Path
import subprocess


def generate_api_docs(project_root_path: Path,
                      labs_list: list[str],
                      rst_docs_root: Path,
                      apidoc_templates_path: Path,
                      overwrite: bool = False) -> None:
    """
    Iterates over all the lab* folders under the project_root_path and
    generates the API .rst document in the corresponding folder under
    rst_docs_root/lab_name

    :param project_root_path:
    :param labs_list:
    :param rst_docs_root:
    :param apidoc_templates_path:
    :param overwrite:
    :return:
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

        print(f'ARGS: {args}')
        result = subprocess.run(args=args)
        if result.returncode == 0:
            print(f'API DOC FOR {lab_path} GENERATED\n')
        else:
            print(f'ERROR WITH CODE: {result.returncode} + {result.stderr}\n')


if __name__ == '__main__':
    project_config = ProjectConfig(config_path=PROJECT_CONFIG_PATH)

    generate_api_docs(project_root_path=PROJECT_ROOT,
                      labs_list=project_config.get_labs_names(),
                      rst_docs_root=PROJECT_ROOT.joinpath('source/docs'),
                      apidoc_templates_path=PROJECT_ROOT.joinpath('templates/apidoc'),
                      overwrite=True)
