"""This module contains the Cookiecutter PyPackage options."""

from __future__ import annotations

__all__ = ("Options",)

from typing import TypedDict


class Options(TypedDict):
    """Cookiecutter PyPackage options."""

    docs: bool
    """Use MkDocs and GitHub Pages."""

    cli: bool
    """Add a command-line interface."""
