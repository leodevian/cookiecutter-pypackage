# {{ cookiecutter.project_name }}

## Installation

Install `{{ cookiecutter.__project_slug }}` using [pip](https://pip.pypa.io/en/stable/):

```console
$ pip install {{ cookiecutter.__project_slug }}
```
{% if cookiecutter.cli %}
## Invocation

Invoke `{{ cookiecutter.__project_slug }}` using [uvx](https://docs.astral.sh/uv/):

```console
$ uvx {{ cookiecutter.__project_slug }}
```
{% endif %}
