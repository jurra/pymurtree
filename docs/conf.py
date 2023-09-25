# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../src/pymurtree'))
# Check path
# print("Path:")
# print(sys.path)

project = 'PyMurTree'
copyright = '2023, Yasel Quintero, Jose Urra, Emir Demirovic, Koos van der Linden'
author = 'Yasel Quintero, Jose Urra, Emir Demirovic, Koos van der Linden'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage'
]

# Specify autodoc settings
# autodoc_member_order = 'bysource'  # Order members by source order
# autodoc_default_options = {
#     'members': True,  # Include members (methods, attributes)
# }

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
