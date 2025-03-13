"""Unit tests for Cookiecutter generation."""

from __future__ import annotations

__all__ = ()

import itertools
import subprocess
from typing import TYPE_CHECKING, Any

import pytest

from tests.utils import context_id

if TYPE_CHECKING:
    from pytest_cookies.plugin import Cookies  # type: ignore[import-untyped]

    from tests.options import Options

SUPPORTED_OPTIONS: list[Options] = [
    {"docs": docs, "cli": cli}
    for docs, cli in itertools.product((False, True), repeat=2)
]


def test_bake(
    cookies: Cookies,
    context: dict[str, Any],
    project_slug: str,
    package_name: str,
) -> None:
    """Test Cookiecutter generation."""
    result = cookies.bake(context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    assert result.project_path.name == project_slug
    package_path = result.project_path / "src" / package_name
    assert package_path.is_dir()


@pytest.mark.parametrize("options", SUPPORTED_OPTIONS, ids=context_id)
def test_options(
    cookies: Cookies,
    context: dict[str, Any],
    package_name: str,
    options: Options,
) -> None:
    """Test Cookiecutter PyPackage options."""
    result = cookies.bake({**context, **options})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    mkdocs_path = result.project_path / "mkdocs.yaml"
    assert mkdocs_path.exists() is options["docs"]

    docs_path = result.project_path / "docs"
    assert docs_path.exists() is options["docs"]

    cli_page_path = docs_path / "api" / f"{package_name}.__main__.md"
    assert cli_page_path.exists() is (options["docs"] and options["cli"])

    package_path = result.project_path / "src" / package_name

    cli_path = package_path / "__main__.py"
    assert cli_path.exists() is options["cli"]


@pytest.mark.integration
@pytest.mark.parametrize("options", SUPPORTED_OPTIONS, ids=context_id)
def test_passes_checks(
    cookies: Cookies,
    context: dict[str, Any],
    options: Options,
) -> None:
    """Test that the generated Python package passes checks."""
    result = cookies.bake({**context, **options})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    try:
        subprocess.run(
            (
                "uvx",
                "--python-preference",
                "only-managed",
                "--python",
                "3.13",
                "--with",
                "tox-uv",
                "tox",
                "run",
                "-m",
                "checks",
            ),
            check=True,
        )

    except subprocess.CalledProcessError:
        pytest.fail("an error occurred", pytrace=True)
