Create a poetry compatible calculation project using calculation-sdk, starflow and metaflow.

# System Requirements
1. python 3.9 +
2. poetry for package and dependency management.

# Python 3.9+
Python is a programming language that lets you work quickly and integrate systems more effectively.
## Home Page
https://www.python.org/  
## Install
https://realpython.com/installing-python/
## Docs
https://docs.python.org/3/

# Python Packaging and Dependency Management
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
## Home Page
https://python-poetry.org/
## Install
https://python-poetry.org/docs/#installation  
## Docs
https://python-poetry.org/docs/  

# Pytest
## Home Page
https://docs.pytest.org/en/7.1.x/index.html
## Install
```commandline
python -m pip install pytest
```
## Docs
https://docs.pytest.org/en/7.1.x/index.html  

about option `--junitxml results.xml` in `pyproject.toml`:  
https://docs.pytest.org/en/7.1.x/how-to/output.html?highlight=junitxml#creating-junitxml-format-files

## Integrate with poetry
https://docs.pytest.org/en/7.1.x/reference/customize.html?pyproject-toml#pyproject-toml

# Coverage
Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
## Home Page
https://coverage.readthedocs.io/en/6.4.1/index.html
## Install
https://coverage.readthedocs.io/en/6.4.1/install.html
## Docs
https://coverage.readthedocs.io/en/6.4.1/index.html
# pytest-cov
## Home Page
https://github.com/pytest-dev/pytest-cov
## Install
https://pytest-cov.readthedocs.io/en/latest/readme.html#installation  
```commandline
python -m pip install pytest-cov
```
## Docs
https://pytest-cov.readthedocs.io/en/latest/index.html   
about option `--cov=calculation-archetype/ --cov-report xml:coverage.xml` in `pyproject.toml`:    
https://pytest-cov.readthedocs.io/en/latest/config.html


# Examples
## Fund Calculation
https://msstash.morningstar.com/projects/DATACALC/repos/calculation-starflow/browse
## Portfolio Calculation
https://msstash.morningstar.com/projects/DATAAPI/repos/cloudy-portfolio-calculations-starflow/browse