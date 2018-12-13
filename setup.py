#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = "0.1.5"


packages = find_packages(
    where="src"
)


# install_requirements = []


setup_requirements = [
    "bumpversion>=0.5",
    "pytest-runner"
]


test_requirements = [
    "pytest>=4.0"
]


extra_requirements = {
    "pytest-plugins": [
        "pytest-flake8",
        "pytest-mypy",
        "pytest-cov"
    ]
}


classifiers = [
    "Development Status :: 4 - Beta"
    "Intended Audience :: Developers"
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


setup(
    name="radixal",
    version=version,
    packages=packages,
    package_dir={'': 'src'},
    url="https://github.com/phuntimes/debased",
    license="MIT License",
    author="Sean McVeigh",
    author_email="spmcveigh@gmail.com",
    description="represent integers with arbitrary radix",
    classifiers=classifiers,
    # install_requires=install_requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require=extra_requirements
)
