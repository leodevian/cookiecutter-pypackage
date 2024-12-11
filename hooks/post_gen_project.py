"""Post-generation hook."""

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    """Run post-generation hook."""
    if Path(".git").exists():
        return

    subprocess.run(("git", "init"), check=True)


if __name__ == "__main__":
    main()
