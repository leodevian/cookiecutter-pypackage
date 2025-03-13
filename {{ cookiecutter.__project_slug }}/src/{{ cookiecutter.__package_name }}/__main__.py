"""The {{ cookiecutter.project_name }} main program."""

from __future__ import annotations

__all__ = ("main",)

import argparse
from typing import TYPE_CHECKING

from {{ cookiecutter.__package_name }} import __version__
from {{ cookiecutter.__package_name }}.log import setup_logging

if TYPE_CHECKING:
    from collections.abc import Sequence

DEFAULT_VERBOSITY = 2


class _Args(argparse.Namespace):
    """Parsed arguments."""

    verbose: int
    """An integer to increase verbosity."""

    quiet: int
    """An integer to decrease verbosity."""

    @property
    def verbosity(self) -> int:
        """Return the verbosity level.

        Returns:
            Verbosity level.
        """
        return max(self.verbose - self.quiet, 0)


def _add_verbosity_options(parser: argparse.ArgumentParser) -> None:
    """Add verbosity options.

    Args:
        parser: Parser.
    """
    verbosity_group = parser.add_argument_group("verbosity")
    verbosity = verbosity_group.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v",
        "--verbose",
        action="count",
        help="increase verbosity",
        default=DEFAULT_VERBOSITY,
    )
    verbosity.add_argument(
        "-q",
        "--quiet",
        action="count",
        help="decrease verbosity",
        default=0,
    )


def _parse_args(argv: Sequence[str] | None = None) -> _Args:
    """Parse command-line arguments.

    Args:
        argv: List of command-line arguments.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    _add_verbosity_options(parser)
    return parser.parse_args(argv, _Args())


def main(argv: Sequence[str] | None = None) -> None:
    """Run the main program.

    Args:
        argv: List of command-line arguments.
    """
    args = _parse_args(argv)
    setup_logging(verbosity=args.verbosity)


if __name__ == "__main__":
    main()
