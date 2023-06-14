# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

#from ebyte_e32.__version__ import VERSION


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CircuitPython Ebyte E32 Library'
copyright = '2023, Herwin Bozet'
author = 'Herwin Bozet'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
]

autodoc_mock_imports = ["busio", "digitalio", "microcontroller"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"
html_css_files = ["extra_styles.css"]

# The short X.Y version.
version = "0.8"
# The full version, including alpha/beta/rc tags.
release = "0.8.0"
