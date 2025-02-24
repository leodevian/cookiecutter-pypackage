"""Post-generation hook."""

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    """Run the post-generation hook.

    It creates an empty Git repository if one does not already exist.
    """
    if Path(".git").exists():
        return

    subprocess.run(("git", "init"), check=True)


if __name__ == "__main__":
    main()
