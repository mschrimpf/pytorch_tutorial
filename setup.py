#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "python>=3.6",
    "numpy",
    "pytorch",
    "torchvision",
    "matplotlib",
    "seaborn",
    "jupyter",
    "tqdm",
]

test_requirements = [
    "pytest",
]

setup(
    name='pytorch-tutorial',
    version='0.1.0',
    long_description=readme,
    author="Martin Schrimpf",
    author_email='msch@mit.edu',
    url='https://github.com/mschrimpf/pytorch_tutorial',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
)
