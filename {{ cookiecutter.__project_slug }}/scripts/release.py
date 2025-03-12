# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "packaging",
#     "towncrier",
# ]
# ///
"""Automation script for releases."""

from __future__ import annotations

import argparse
import subprocess
from typing import TYPE_CHECKING

from packaging.version import Version

if TYPE_CHECKING:
    from collections.abc import Sequence


class Args(argparse.Namespace):
    """Parsed arguments."""

    version: Version
    """Target version."""

    dry_run: bool
    """Perform dry run."""


def parse_args(argv: Sequence[str] | None = None) -> Args:
    """Parse arguments.

    Args:
        argv: List of command-line arguments.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Prepare a new release.")
    parser.add_argument(
        "--version",
        type=Version,
        required=True,
        help="Target version.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run.",
    )
    return parser.parse_args(argv, Args())


def main(argv: Sequence[str] | None = None) -> None:
    """Prepare a new release.

    Args:
        argv: List of command-line arguments.
    """
    args = parse_args(argv)

    subprocess.run(("git", "diff", "--quiet"), check=True)

    base_branch = subprocess.run(
        ("git", "rev-parse", "--abbrev-ref", "HEAD"),
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()

    release_branch = f"releases/{args.version.public}"

    subprocess.run(("git", "switch", "-c", release_branch), check=True)

    try:
        release_notes = subprocess.run(
            ("towncrier", "build", "--draft", "--version", args.version.public),
            capture_output=True,
            check=True,
            text=True,
        ).stdout

        subprocess.run(
            ("towncrier", "build", "--yes", "--version", args.version.public),
            check=True,
        )
        subprocess.run(
            ("git", "add", "-A", ":/CHANGELOG.md", ":/changelog.d"),
            check=True,
        )
        subprocess.run(
            (
                "git",
                "commit",
                "-m",
                f"build: bump version to {args.version.public}",
                "--no-verify",
            ),
            check=True,
        )

    except subprocess.CalledProcessError:
        subprocess.run(("git", "switch", base_branch), check=True)
        subprocess.run(("git", "branch", "-d", release_branch), check=True)
        raise

    if not args.dry_run:
        subprocess.run(
            ("git", "push", "--set-upstream", "origin", release_branch),
            check=True,
        )

    subprocess.run(
        (
            "gh",
            "pr",
            "create",
            "--base",
            base_branch,
            "--title",
            f"Release {args.version.public}",
            "--body",
            release_notes,
            *(("--dry-run",) if args.dry_run else ()),
        ),
        check=True,
    )

    if not args.dry_run:
        subprocess.run(
            (
                "gh",
                "pr",
                "merge",
                release_branch,
                "--auto",
                "--rebase",
                "--delete-branch",
            ),
            check=True,
        )


if __name__ == "__main__":
    main()
