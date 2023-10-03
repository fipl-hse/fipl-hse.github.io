import os
import shutil
import subprocess
from pathlib import Path

from config.constants import (PROJECT_ROOT,
                              API_DOC_TEMPLATES_PATH,
                              RST_DOCS_ROOT,
                              PROJECT_CONFIG,
                              DOC_BUILD_DIR,
                              WEBSITE_ROOT)
from tools.docs_generator.generate_api_docs import generate_api_docs


def build_documentation(build_directory: Path) -> None:
    """Build full website with lab & API docs

    Args:
        build_directory:

    Returns:

    """
    print(f'Clearing docs build directory: {build_directory}')
    shutil.rmtree(path=build_directory, ignore_errors=True)

    os.makedirs(name=build_directory,
                exist_ok=True)

    print(f'Generating API docs...')
    generate_api_docs(project_root_path=PROJECT_ROOT,
                      labs_list=PROJECT_CONFIG.get_labs_names(),
                      rst_docs_root=RST_DOCS_ROOT,
                      apidoc_templates_path=API_DOC_TEMPLATES_PATH,
                      overwrite=True)

    print(f'Building documentation...')
    args = [
        'sphinx-build',
        '-b',
        'html',
        WEBSITE_ROOT,
        build_directory
    ]
    print(f'HTML BUILD COMMAND: {" ".join(map(str, args))}')
    result_html = subprocess.run(args=args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result_html.returncode != 0:
        print(f'There are problems with building html: {result_html.stdout}')

    args = [
        'sphinx-build',
        '-b',
        'docx',
        WEBSITE_ROOT,
        build_directory
    ]
    print(f'DOCX BUILD COMMAND: {" ".join(map(str, args))}')
    result_docs = subprocess.run(args=args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
