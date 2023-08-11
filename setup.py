#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/12/23 3:17 PM
# @Author  : zhangchao
# @File    : setup.py
# @Email   : zhangchao5@genomics.cn

import setuptools

__version__ = "0.1.3"

requirements = open("requirements.txt").readline()


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spatialign",
    version=__version__,
    author="zhangchao5",
    author_email="zhangchao5@genomics.cn",
    description="An Unsupervised Contrastive Learning Model for Data Integration of Spatially Resolved Transcriptomics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/STOmics/Spatialign.git",
    packages=setuptools.find_packages(),
    package_data={'': ["*.so"]},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
)

