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
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = '\\textbf{Addressing Uncertainty in MultiSector Dynamics Research}'
copyright = '2021, Battelle Memorial Institute'

# The full version, including alpha/beta/rc tags
release = 'v0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'nbsphinx'
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

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# theme options for alabaster
html_theme_options = {
    'note_bg': '#D6EAF8',
    'seealso_bg': '#D6EAF8'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# add in the IM3 logo into the top left sidebar if so desired
# html_theme_options = {
#     'logo': 'im3.png'
# }

# -- Options for Latex
master_doc = 'index'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = None


latex_documents = [
    (master_doc, 'addressinguncertaintyinmultisectordynamicsresearch.tex', project,
     'Patrick M. Reed, Antonia Hadjimichael, Keyvan Malek'
     '\\and Tina Karimi, Chris R. Vernon, Vivek Srikrishnan'
     '\\and Rohini Gupta, David Gold, B. Lee, Klaus Keller, Jennie S. Rice'
     , 'book'),
]

latex_elements = {
    'papersize': 'a4paper',
    'releasename': release
}
