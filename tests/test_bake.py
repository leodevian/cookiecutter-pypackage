"""Unit tests for Cookiecutter generation."""

from __future__ import annotations

__all__ = ()

from typing import TYPE_CHECKING, Any

import pytest
from slugify import slugify

from tests.utils import context_id

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

    package_name = slugify(context["project_name"], separator="_")
    assert (result.project_path / "src" / package_name).is_dir()


@pytest.mark.parametrize(
    "docs",
    [
        False,
        True,
    ],
)
def test_docs(
    cookies: Cookies,
    context: dict[str, Any],
    docs: bool,
) -> None:
    """Test the option to use MkDocs and GitHub Pages."""
    result = cookies.bake(extra_context={**context, "docs": docs})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert (result.project_path / "docs").is_dir() is docs
    assert (result.project_path / "mkdocs.yaml").exists() is docs


@pytest.mark.parametrize(
    "cli",
    [
        False,
        True,
    ],
)
def test_cli(
    cookies: Cookies,
    context: dict[str, Any],
    cli: bool,
) -> None:
    """Test the option to add a command-line interface."""
    result = cookies.bake(extra_context={**context, "cli": cli, "docs": True})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    package_name = slugify(context["project_name"], separator="_")
    assert (result.project_path / "src" / package_name / "__main__.py").exists() is cli
    assert (
        result.project_path / "docs" / "api" / f"{package_name}.__main__.md"
    ).exists() is cli
