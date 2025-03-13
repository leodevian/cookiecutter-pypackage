"""The logging setup."""

from __future__ import annotations

__all__ = ("setup_logging",)

import logging

_LEVELS = {
    0: logging.CRITICAL,
    1: logging.ERROR,
    2: logging.WARNING,
    3: logging.INFO,
    4: logging.DEBUG,
    5: logging.NOTSET,
}

_MAX_LEVEL = max(_LEVELS)


def _get_level(verbosity: int) -> int:
    """Return log level from verbosity level.

    Args:
        verbosity: Verbosity level.

    Returns:
        Log level.
    """
    return _LEVELS[min(verbosity, _MAX_LEVEL)]


def setup_logging(verbosity: int) -> logging.Logger:
    """Setup logging.

    Args:
        verbosity: Verbosity level.

    Returns:
        Logger.
    """
    logger = logging.getLogger("{{ cookiecutter.__package_name }}")
    level = _get_level(verbosity)
    logger.setLevel(logging.DEBUG)
    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)
    return logger
