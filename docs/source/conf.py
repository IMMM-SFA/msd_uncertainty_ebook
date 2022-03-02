# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../../'))
sys.path.append(os.path.abspath("../../extensions"))

# current datetime to use as the version
today = f"Last updated: {datetime.utcnow().strftime('%b %d, %Y')}"


# -- Project information -----------------------------------------------------

project = 'Addressing Uncertainty in MultiSector Dynamics Research'
copyright = '2022, Battelle Memorial Institute'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.bibtex',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'nbsphinx',
    'appendix'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# bibliography files
bibtex_bibfiles = ['refs.bib']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']

# Figures and tables are automatically numbered if they have a caption.
# This also helps with referencing figures in the main text (otherwise
# the link text is the figure caption).
numfig = True

numfig_format = {
    'section': 'Chapter %s',
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# theme options
html_theme_options = {
    'path_to_docs': '/docs',
    'repository_url': 'https://github.com/IMMM-SFA/msd_uncertainty_ebook',
    'use_issues_button': True,
    'use_download_button': True,
    'use_repository_button': True,
    'extra_navbar': f'<span style="display:block;text-align:left">{today}</span>',
    'home_page_in_toc': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# -- Options for Latex
master_doc = 'index'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = None

latex_elements = {
    'releasename': '',
    'tableofcontents': '',
    'maketitle': '',
}

latex_documents = [
    (master_doc,
     'addressinguncertaintyinmultisectordynamicsresearch.tex',
     '\\textbf{Addressing Uncertainty in MultiSector Dynamics Research}',
     'Patrick M. Reed, Antonia Hadjimichael, Keyvan Malek'
     '\\and Tina Karimi, Chris R. Vernon, Vivek Srikrishnan, Rohini S. Gupta'
     '\\and David F. Gold, Ben Lee, Klaus Keller, Jennie S. Rice, Travis B. Thurber',
     'book')
]
