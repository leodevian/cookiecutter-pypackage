# {{ cookiecutter.project_name }}

- GitHub repository: <{{ cookiecutter.__github_repository }}>
{%- if cookiecutter.docs %}
- Documentation: <{{ cookiecutter.__github_pages }}>
{%- endif %}
- License: {{ cookiecutter.license }}

## Installation

Install `{{ cookiecutter.__project_slug }}` using [pip](https://pip.pypa.io/en/stable/):

```console
$ pip install {{ cookiecutter.__project_slug }}
```
