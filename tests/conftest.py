"""This module contains fixtures."""

from __future__ import annotations

__all__ = ()

from typing import Any

import pytest


@pytest.fixture
def context() -> dict[str, Any]:
    """Generate context."""
    return {
        "project_name": "My Python Package",
        "author_name": "Léo Bernard",
        "author_email": "leodevian.gh@gmail.com",
        "github_owner": "leodevian",
    }
