"""This module contains fixtures."""

from __future__ import annotations

__all__ = ()

from typing import Any

import pytest
from slugify import slugify


@pytest.fixture
def context() -> dict[str, Any]:
    """Generate context."""
    return {
        "project_name": "My Python Package",
        "author_name": "Léo Bernard",
        "author_email": "leodevian.gh@gmail.com",
        "github_owner": "leodevian",
        "docs": False,
        "cli": False,
    }


@pytest.fixture
def project_slug(context: dict[str, Any]) -> str:
    """Return the project slug."""
    return slugify(context["project_name"])


@pytest.fixture
def package_name(project_slug: str) -> str:
    """Return the package name."""
    return project_slug.replace("-", "_")
