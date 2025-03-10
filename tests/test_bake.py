"""Unit tests for Cookiecutter generation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest
from slugify import slugify

if TYPE_CHECKING:
    from pytest_cookies.plugin import Cookies  # type: ignore[import-untyped]


@pytest.fixture
def context() -> dict[str, Any]:
    """Generate context."""
    return {
        "project_name": "My Python Package",
        "author_name": "Léo Bernard",
        "author_email": "leodevian.gh@gmail.com",
        "github_owner": "leodevian",
    }


def context_id(context: dict[str, Any]) -> str:
    """Create test ID from context."""
    return "-".join(f"{key}:{value}" for key, value in context.items())


@pytest.mark.parametrize(
    "context_override",
    [
        {"license": "MIT"},
        {"license": "BSD-3-Clause"},
        {"license": "GPL-3.0-only"},
        {"license": "Apache-2.0"},
        {"license": "LicenseRef-Proprietary"},
    ],
    ids=context_id,
)
def test_bake(
    cookies: Cookies,
    context: dict[str, Any],
    context_override: dict[str, Any],
) -> None:
    """Test that the Python package is generated."""
    result = cookies.bake(
        extra_context={
            **context,
            **context_override,
        },
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == slugify(context["project_name"])
    assert result.project_path.is_dir()
