# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python packages.

- GitHub repository: https://github.com/leodevian/cookiecutter-pypackage
- Documentation: https://github.com/leodevian/cookiecutter-pypackage/tree/main/docs
- License: MIT

## Features

- License choice
- Testing setup with [pytest](https://docs.pytest.org/en/stable/index.html)
- Code coverage endorsed by [Codecov](https://about.codecov.io/)
- Automated testing with [tox](https://tox.wiki/en/stable/)
- Type checking with [mypy](https://mypy.readthedocs.io/en/stable/)
- Git hooks setup with [pre-commit](https://pre-commit.com/)
  - Prevent large files from being committed with [check-added-large-files](https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md#check-added-large-files)
  - Check for files with names that would conflict on a case-insensitive filesystem with [check-case-conflict](https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md#check-case-conflict)
  - Check for files that contain merge conflict strings with [check-merge-conflict](https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md#check-merge-conflict)
  - Check for symlinks which do not point to anything with [check-symlinks](https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md#check-symlinks)
  - Replace or check mixed line ending with [mixed-line-ending](https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md#mixed-line-ending)
  - Verify syntax for TOML files with [check-toml](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#check-toml)
  - Verify syntax for YAML files with [check-yaml](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#check-yaml)
  - Make sure files end in a newline and only a newline with [end-of-file-fixer](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#end-of-file-fixer)
  - Trim trailing whitespaces with [trailing-whitespace](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#trailing-whitespace)
  - Lint with [the Ruff linter](https://docs.astral.sh/ruff/linter/)
  - Format code with [the Ruff formatter](https://docs.astral.sh/ruff/formatter/)
  - Run [Black](https://black.readthedocs.io/en/stable/) on Python code blocks in documentation with [blacken-docs](https://github.com/adamchainz/blacken-docs)
  - Type check with [mypy](https://mypy.readthedocs.io/en/stable/)
  - Fix common misspellings with [codespell](https://github.com/codespell-project/codespell)
  - Check for missing [docstrings](https://peps.python.org/pep-0257/) with [interrogate](https://interrogate.readthedocs.io/en/latest/)
- Ready for generation documentation with [MkDocs](https://www.mkdocs.org/)
  and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
  - Automatic documentation from sources with [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
- Changelog based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) with [towncrier](https://towncrier.readthedocs.io/en/stable/tutorial.html)
- Semantic versioning with [bump-my-version](https://github.com/callowayproject/bump-my-version/tree/b00f3dd1ce6b12f3e5b302ce7292d9714740fd96)
- Creation of an empty Git repository (optional)
- Creation of a development environment with [uv](https://docs.astral.sh/uv/) (optional)
- Installation of [pre-commit](https://pre-commit.com/) hooks (optional)

## Quickstart

Run the following command to generate your Python package.

```bash
uvx cookiecutter https://github.com/leodevian/cookiecutter-pypackage.git
```
