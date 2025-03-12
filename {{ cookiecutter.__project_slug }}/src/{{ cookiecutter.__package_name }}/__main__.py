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


def main(argv: Sequence[str] | None = None) -> None:
    """Run the main program.

    Args:
        argv: List of command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv, _Args())
    print(args)  # noqa: T201


if __name__ == "__main__":
    main()
