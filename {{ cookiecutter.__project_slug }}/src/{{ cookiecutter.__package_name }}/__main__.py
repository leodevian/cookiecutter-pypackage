"""The {{ cookiecutter.project_name }} main program."""

from __future__ import annotations

__all__ = ("main",)

import argparse
from typing import TYPE_CHECKING

from {{ cookiecutter.__package_name }} import __version__

if TYPE_CHECKING:
    from collections.abc import Sequence


class _Args(argparse.Namespace):
    """Parsed arguments."""


def _parse_args(argv: Sequence[str] | None = None) -> Args:
    """Parse command-line arguments.

    Args:
        argv: List of command-line arguments.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    return parser.parse_args(argv, _Args())


def main(argv: Sequence[str] | None = None) -> None:
    """Run the main program.

    Args:
        argv: List of command-line arguments.
    """
    _parse_args(argv)


if __name__ == "__main__":
    main()
