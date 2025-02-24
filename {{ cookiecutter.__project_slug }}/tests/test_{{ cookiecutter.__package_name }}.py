"""Unit tests for `{{ cookiecutter.__package_name }}`."""

from {{ cookiecutter.__package_name }} import hello


def test_hello() -> None:
    """Test the hello message."""
    assert hello("{{ cookiecutter.author_name }}") == "Hello {{ cookiecutter.author_name }}!"
