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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Manta'
copyright = '2024, Alexander Nasuta'
author = 'Alexander Nasuta'

# The full version, including alpha/beta/rc tags
release = '0.6.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx_copybutton",

    "sphinx.ext.autosectionlabel",

    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",

    "sphinx.ext.autodoc",

    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",

    "manta.docbuild.manta_directive",

    "nbsphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'custom_colors.css',
    'custom_font.css',
]
html_logo = "_static/logo.png"
html_theme_options = {
    "light_css_variables": {
        #"font-stack": "Changa, sans-serif",
        #"font-stack--monospace": "Roboto Mono, monospace",
        #"color-foreground-primary": "#dddddd",  # main text and headings
        #"color-foreground-secondary": "#cccccc",  # secondary text
        #"color-foreground-muted": "#d0d0d0",  # muted text
        #"color-foreground-border": "#923eb1",  # for content borders
        #"color-background-primary": "#160f30",  # for content
        #"color-background-secondary": "#201146",  # for navigation + ToC
        #"color-background-hover": "#4f4fb0",  # for navigation-item hover
        #"color-background-hover--transparent": "#4f4fb000",
        #"color-background-border": "#403333",  # for UI borders
        #"color-background-item": "#411a30",  # for "background" items (eg: copybutton)
        #"color-announcement-background": "#000000dd",  # announcements
        #"color-announcement-text": "#eeebee",  # announcements
        #"color-admonition-title-background--note": "#FFFFFF33",  # Note background
        #"color-admonition-title-background--warning": "#FF000033",  # Warning background
        #"color-admonition-background": "#FFFFFF11",  # Admonition backgrounds
        #"color-brand-primary": "#eeeeee",  # brand colors (sidebar titles)
        #"color-brand-content": "#00dfef",  # brand colors (hyperlink color)
        #"color-highlight-on-target": "#333300",  # Highlighted text background
    },
    "dark_css_variables": {
        #"font-stack": "Changa, sans-serif",
        #"font-stack--monospace": "Roboto Mono, monospace",
        #"color-foreground-primary": "#dddddd",  # main text and headings
        #"color-foreground-secondary": "#cccccc",  # secondary text
        #"color-foreground-muted": "#d0d0d0",  # muted text
        #"color-foreground-border": "#923eb1",  # for content borders
        #"color-background-primary": "#160f30",  # for content
        #"color-background-secondary": "#201146",  # for navigation + ToC
        #"color-background-hover": "#4f4fb0",  # for navigation-item hover
        #"color-background-hover--transparent": "#4f4fb000",
        #"color-background-border": "#403333",  # for UI borders
        #"color-background-item": "#411a30",  # for "background" items (eg: copybutton)
        #"color-announcement-background": "#000000dd",  # announcements
        #"color-announcement-text": "#eeebee",  # announcements
        #"color-admonition-title-background--note": "#FFFFFF33",  # Note background
        #"color-admonition-title-background--warning": "#FF000033",  # Warning background
        #"color-admonition-background": "#FFFFFF11",  # Admonition backgrounds
        #"color-brand-primary": "#eeeeee",  # brand colors (sidebar titles)
        #"color-brand-content": "#00dfef",  # brand colors (hyperlink color)
        #"color-highlight-on-target": "#333300",  # Highlighted text background
    }
    #"sidebar_hide_name": False,
    #"navigation_with_keys": True,
    #'collapse_navigation': False,
    #'navigation_depth': 4,
}

# Import the necessary module
from sphinx.ext import autosectionlabel

# Configure autosectionlabel
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Exclude specific files
autosectionlabel_exclude_files = ['README.md']