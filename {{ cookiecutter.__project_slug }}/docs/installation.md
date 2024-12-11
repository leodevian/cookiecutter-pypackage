# Installation

## Stable release

Run the following command to install `{{ cookiecutter.__project_slug }}`.

=== "uv"

    ```bash
    uv add {{ cookiecutter.__project_slug }}
    ```

=== "pip"

    ```bash
    pip install {{ cookiecutter.__project_slug }}
    ```

This installation method will always install the latest stable release.

## From sources

You can clone the repository.

```bash
git clone {{ cookiecutter.__github_repository }}.git
```

Then, you can run the following command to install it.

=== "uv"

    ```bash
    uv sync
    ```

=== "pip"

    ```bash
    pip install .
    ```
