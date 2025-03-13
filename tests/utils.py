"""This module contains helper functions."""

from __future__ import annotations

__all__ = ("context_id",)

from typing import Any


def context_id(context: dict[str, Any]) -> str:
    """Create test ID from context."""
    return "-".join(f"{key}:{value}" for key, value in context.items())
