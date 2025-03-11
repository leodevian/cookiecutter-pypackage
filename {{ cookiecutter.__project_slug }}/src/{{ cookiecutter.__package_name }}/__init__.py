"""{{ cookiecutter.short_description or cookiecutter.project_name }}."""

from __future__ import annotations

__all__ = ("__version__",)

import importlib.resources


def _get_version() -> str:
    """Read `VERSION.txt` and return its contents.

    Returns:
        Version string.
    """
    files = importlib.resources.files("{{ cookiecutter.__package_name }}")
    return (files / "VERSION.txt").read_text(encoding="utf-8")


__version__ = _get_version()
