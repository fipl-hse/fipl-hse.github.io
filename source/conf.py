# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pathlib import Path
import sys

project_root = Path('..').resolve()
sys.path.insert(0, str(project_root))

project = 'Программирование для лингвистов'
copyright = '2023, Демидовский А.В. и другие'
author = 'Демидовский А.В. и другие'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'docxbuilder',
    'sphinx.ext.napoleon',
    'sphinx_tabs.tabs',
    'notfound.extension',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    "torch": ("https://pytorch.org/docs/stable", '../config/intersphinx/pytorch.inv'),
    'python': ('https://docs.python.org/3', None),
    "pandas": ('http://pandas.pydata.org/pandas-docs/stable/', '../config/intersphinx/pandas.inv'),
    "pydantic": ('https://docs.pydantic.dev/latest/', '../config/intersphinx/pydantic.inv'),
    "fastapi": ('https://fastapi.tiangolo.com/', '../config/intersphinx/fastapi.inv'),
}

templates_path = ['_templates']
exclude_patterns = []

# Template used to render the 404.html generated by this extension.
# notfound_template = "404.html"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
# html_title = project
html_logo = '_static/fal_logo.jpeg'
