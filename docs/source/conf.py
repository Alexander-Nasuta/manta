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
release = '0.8.0'

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
    'manim.css',
    #'custom_font.css',
    # 'manta.css',
]

html_title = f"Manta v{release}"
html_logo = "_static/logo.png"
# html_theme_options
_ = {
    # "source_repository": "",
    # "source_branch": "main",
    # "source_directory": "docs/source/",
    # "light_logo": "manim-logo-sidebar.svg",
    # "dark_logo": "manim-logo-sidebar-dark.svg",
    "light_css_variables": {
        "color-content-foreground": "#4c4f69",  # Text
        "color-background-primary": "#eff1f5",  # Base
        "color-background-border": "#ccd0da",  # Surface0
        "color-sidebar-background": "#e6e9ef",  # Mantle
        "color-brand-content": "#7287fd",  # Lavender
        "color-brand-primary": "#04a5e5",  # Sky
        "color-link": "#1e66f5",  # Blue
        "color-link--hover": "#8839ef",  # Mauve
        "color-inline-code-background": "#f6f6f6",  # Keeping the original as no direct match
        "color-foreground-secondary": "#209fb5",  # Sapphire

        "color-admonition-title-background--warning": "rgba(254, 100, 11, 0.2)",  # Peach
        "color-admonition-title--warning": "#fe640b",  # Peach

        "color-admonition-title-background--note": "rgba(4, 165, 229, 0.2)",  # Sky
        "color-admonition-title--note": "#04a5e5",  # Sky

        "color-admonition-title-background--tip": "rgba(64, 160, 43, 0.2)",  # Green
        "color-admonition-title--tip": "#40a02b",  # Green

        "color-admonition-title-background--seealso": "rgba(30, 102, 245, 0.2)",  # Blue
        "color-admonition-title--seealso": "#1e66f5",  # Blue

        "color-sidebar-search-background": "#e6e9ef",  # Mantle
    },
    "dark_css_variables": {
        "color-content-foreground": "#cdd6f4",  # Text
        "color-background-primary": "#1e1e2e",  # Base
        "color-background-border": "#313244",  # Surface0
        "color-sidebar-background": "#181825",  # Mantle
        "color-brand-content": "#b4befe",  # Lavender
        "color-brand-primary": "#89dceb",  # Sky
        "color-link": "#89b4fa",  # Blue
        "color-link--hover": "#cba6f7",  # Mauve
        "color-inline-code-background": "#313244",  # Surface0
        "color-foreground-secondary": "#74c7ec",  # Sapphire

        "color-admonition-title-background": "rgba(203, 166, 247, 0.2)",  # Mauve
        "color-admonition-title": "rgb(203, 166, 247)",  # Mauve


        "color-admonition-title-background--warning": "rgba(250, 179, 135, 0.2)",  # Peach
        "color-admonition-title--warning": "#fab387",  # Peach

        "color-admonition-title-background--note": "rgba(137, 220, 235, 0.2)",  # Sky
        "color-admonition-title--note": "#89dceb",  # Sky

        "color-admonition-title-background--tip": "rgba(166, 227, 161, 0.2)",  # Green
        "color-admonition-title--tip": "#a6e3a1",  # Green

        "color-admonition-title-background--seealso": "rgba(137, 180, 250, 0.2)",  # Blue
        "color-admonition-title--seealso": "#89b4fa",  # Blue

        "color-sidebar-search-background": "#181825",  # Mantle

        "color-code-background": "#313244", # Base
        "code-example-bg": "#313244", # Base

    },
    "sidebar_hide_name": False,
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
