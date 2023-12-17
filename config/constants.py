"""
Useful constant variables
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PROJECT_CONFIG_PATH = PROJECT_ROOT / 'config' / 'project_config.json'

SOURCE_CODE_ROOT = PROJECT_ROOT.joinpath('labs')

DOC_BUILD_DIR = PROJECT_ROOT.joinpath('source').joinpath('build')
WEBSITE_ROOT = PROJECT_ROOT.joinpath('source')
RST_DOCS_ROOT = WEBSITE_ROOT.joinpath('docs')
API_DOC_TEMPLATES_PATH = PROJECT_ROOT.joinpath('templates/apidoc')
