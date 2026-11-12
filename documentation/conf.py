"""
file: documentation/conf.py
brief: Sphinx documentation build configuration file for the Harpy
project.

This file is part of the Harpy project and is licensed under the
3-Clause BSD License;
For more information, see LICENSE.txt.
"""

project: str = "The Harpy Documentation"
copyright: str = "2026, Ismael Moreira"
author: str = "Ismael Moreira"
release: str = "v0.1.0"
html_theme: str = "sphinx_rtd_theme"
html_favicon: str = "_static/images/logo.png"
exclude_patterns: list[str] = []
html_static_path: list[str] = ["_static"]
templates_path: list[str] = ["_templates"]
extensions: list[str] = [
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "breathe",
]
breathe_projects: dict[str, str] = {"Harpy": "../build/documentation/xml"}
breathe_default_project: str = "Harpy"
