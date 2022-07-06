# Python Packaging and Dependency Management
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
## Home Page
https://python-poetry.org/
## Install
https://python-poetry.org/docs/#installation  
## Docs
https://python-poetry.org/docs/ 

## What is the difference for `dependencies`, `dev-dependencies` and `extras`?
`tool.poetry.dependencies` contains dependencies that are required for the final product.

`tool.poetry.dev-dependencies` contains dependencies that are required for developers working on this project. These dependencies are not needed for the final product, but only for the development and testing of the application. Finally, the fourth section is the build-system section, which contains settings for the build system.

`tool.poetry.extras` supports extras to allow expression of: 1) optional dependencies, which enhance a package, but are not required; 2) clusters of optional dependencies.

