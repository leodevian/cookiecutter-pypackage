"""Post-generation hook."""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def remove_module(module_name: str) -> None:
    """Remove a module from the Python package and remove its API reference page."""
    package_name = "{{ cookiecutter.__package_name }}"  # rendered
    Path("src", package_name, f"{module_name}.py").unlink(missing_ok=True)
    Path("docs", "api", f"{package_name}.{module_name}.md").unlink(missing_ok=True)


def remove_read_only(func: Callable[..., Any], path: str, _: Any) -> None:  # noqa: ANN401
    """Clear the read-only bit and reattempt the removal.

    See https://docs.python.org/3/library/shutil.html#rmtree-example.
    """
    os.chmod(path, stat.S_IWRITE)  # noqa: PTH101
    func(path)


def force_remove_directory(dir_path: Path) -> None:
    """Force remove a directory."""
    if sys.version_info < (3, 12):
        shutil.rmtree(dir_path, onerror=remove_read_only)
    else:
        shutil.rmtree(dir_path, onexc=remove_read_only)


def remove_documentation() -> None:
    """Remove MkDocs documentation."""
    mkdocs_path = Path("mkdocs.yaml")
    mkdocs_path.unlink(missing_ok=True)
    docs_path = Path("docs")
    force_remove_directory(docs_path)


def create_empty_git_repository() -> None:
    """Create an empty Git repository.

    Do nothing if one already exists.
    """
    if Path(".git").exists():
        return

    subprocess.run(("git", "init", "-b", "main"), check=True)


def main() -> None:
    """Run the post-generation hook."""
    create_empty_git_repository()

    if "{{ cookiecutter.docs }}" != "True":
        remove_documentation()

    if "{{ cookiecutter.cli }}" != "True":
        remove_module("__main__")


if __name__ == "__main__":
    main()
