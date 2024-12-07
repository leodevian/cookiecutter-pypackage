"""Pre-generation hook."""

import re

TERMINATOR = "\x1b[0m"
ERROR = "\x1b[1;91m [ERROR]: "
HINT = "\x1b[3;33m"

PACKAGE_NAME_PATTERN = r"[a-z][_a-z0-9]+"
VERSION_PATTERN = r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"


def check_package_name(package_name: str) -> None:
    """Check a package name.

    Args:
        package_name: Package name.

    Raises:
        ValueError: Invalid package name.
    """
    if not re.match(f"^{PACKAGE_NAME_PATTERN}$", package_name):
        raise ValueError(f"Invalid package name: {package_name!r}")


def check_version(version: str) -> None:
    """Check a version string.

    Args:
        version: Version string.

    Raises:
        ValueError: Invalid version.
    """
    if not re.match(f"^{VERSION_PATTERN}$", version, re.VERBOSE | re.IGNORECASE):
        raise ValueError(f"Invalid version: {version!r}")


if __name__ == "__main__":
    success = True

    try:
        check_package_name("{{ cookiecutter.__package_name }}")

    except ValueError as e:
        success = False
        print(f"{ERROR}{e}{TERMINATOR}")
        print(
            f"{HINT}"
            "Per PEP 8, Python packages should also have short, all-lowercase names, "
            "although the use of underscores is discouraged."
            f"{TERMINATOR}"
        )

    try:
        check_version("{{ cookiecutter.version }}")

    except ValueError as e:
        success = False
        print(f"{ERROR}{e}{TERMINATOR}")

    if not success:
        raise SystemExit(1)
