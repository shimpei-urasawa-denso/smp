# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2025, s'
author = 's'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_needs"]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# -- Options for sphinx-needs ----------------------
needs_extra_options = [
   {
    "name": "image", 
    "type": "string"
   }
]
needs_types = [
    {
        "directive": "req",
        "title": "Requirement",
        "prefix": "R_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "spec",
        "title": "Specification",
        "prefix": "S_",
        "color": "##EDCD2",
        "style": "node",
    },
    {
        "directive": "tutorial-project",
        "title": "Project",
        "prefix": "P_",  # prefix for auto-generated IDs
        "style": "rectangle", # style for the type in diagrams
        "color": "#BFD8D2", # color for the type in diagrams
    }
]

needs_extra_links = [
  {
    "option": "tutorial_required_by",
    "incoming": "requires",  # text to describe incoming links
    "outgoing": "required by",  # text to describe outgoing links
    "style": "#00AA00",  # color for the link in diagrams
  },
  {
    "option": "tutorial_specifies_by",
    "incoming": "specify",  # text to describe incoming links
    "outgoing": "specified by",  # text to describe outgoing links
    "style": "#00AA00",  # color for the link in diagrams
  },
]


