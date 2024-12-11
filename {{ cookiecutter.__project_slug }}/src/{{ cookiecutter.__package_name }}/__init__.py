"""{{ cookiecutter.short_description or cookiecutter.project_name }}."""

__all__ = ("__version__",)

from {{ cookiecutter.__package_name }}._version import version as __version__
