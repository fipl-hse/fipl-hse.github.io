from pathlib import Path
import sys

project_root = Path(__file__).parent.parent.resolve()
print(f"{project_root=}")
sys.path.insert(0, str(project_root))
print(sys.path)

project = 'Программирование для лингвистов'
copyright = '2023, Демидовский А.В. и другие'
author = 'Демидовский А.В. и другие'

extensions = [
    'docxbuilder',
    'notfound.extension',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib.plantuml',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

intersphinx_mapping = {
    "torch": ("https://pytorch.org/docs/stable", "../config/intersphinx/pytorch.inv"),
    "python": ("https://docs.python.org/3", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", "../config/intersphinx/pandas.inv"),
    "pydantic": ("https://docs.pydantic.dev/latest/", "../config/intersphinx/pydantic.inv"),
    "fastapi": ("https://fastapi.tiangolo.com/", "../config/intersphinx/fastapi.inv"),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "networkx": ("https://networkx.org/documentation/stable", None)
}

nitpick_ignore = [
    ('py:class', 'spacy.tokens.token.Token'),
    ('py:class', 'spacy.tokens.Token'),
    ('py:class', 'DiGraph'),
    ("py:class", "Doc"),
    ("py:class", "Language"),
    ("py:class", "spacy.language.Language"),
    ("py:class", "spacy.tokens.doc.Doc"),
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_typehints = "description"

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_logo = '_static/fal_logo.jpeg'
