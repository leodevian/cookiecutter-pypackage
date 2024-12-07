"""Post-generation hook."""

import subprocess

TERMINATOR = "\x1b[0m"
ERROR = "\x1b[1;91m [ERROR]: "
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"


def create_git_repository() -> None:
    """Create an empty Git repository."""
    subprocess.run(["git", "init"], check=True)


def create_dev_venv() -> None:
    """Create a development environment."""
    subprocess.run(["uv", "sync"], check=True)


def install_pre_commit_hooks() -> None:
    """Install pre-commit hooks."""
    subprocess.run(
        ["uv", "run", "--isolated", "--group", "lint", "pre-commit", "install"],
        check=True,
    )


if __name__ == "__main__":
    git_init = False

    if "{{ cookiecutter.git_init }}" == "True":  # type: ignore[comparison-overlap]  # noqa: PLR0133
        try:
            print(f"{INFO}Creating an empty Git repository...{TERMINATOR}")
            create_git_repository()

        except Exception:  # noqa: BLE001
            print(f"{ERROR}Failed to create an empty Git repository{TERMINATOR}")
            print(f"{HINT}Did you install Git?{TERMINATOR}")

        else:
            git_init = True
            print(f"{SUCCESS}An empty Git repository has been created{TERMINATOR}")

    if "{{ cookiecutter.uv_sync }}" == "True":  # type: ignore[comparison-overlap]  # noqa: PLR0133
        try:
            print(f"{INFO}Creating a development environment...{TERMINATOR}")
            create_dev_venv()

        except Exception:  # noqa: BLE001
            print(f"{ERROR}Failed to create a development environment{TERMINATOR}")
            print(f"{HINT}Did you install uv?{TERMINATOR}")

        else:
            print(f"{SUCCESS}A development environment has been created{TERMINATOR}")

    if git_init and "{{ cookiecutter.pre_commit_install }}" == "True":  # type: ignore[comparison-overlap]  # noqa: PLR0133
        try:
            print(f"{INFO}Installing pre-commit hooks...{TERMINATOR}")
            install_pre_commit_hooks()

        except Exception:  # noqa: BLE001
            print(f"{ERROR}Failed to install pre-commit hooks{TERMINATOR}")
            print(f"{HINT}Did you install uv?{TERMINATOR}")

        else:
            print(f"{SUCCESS}pre-commit hooks have been installed{TERMINATOR}")
