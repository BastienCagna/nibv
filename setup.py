#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

verstr = "0.0.1"


setup(
    name="nibv",
    version=verstr,
    packages=find_packages(),
    author="Bastien Cagna",
    description="NiPype automatic wrapping for BrainVISA processes",
    install_requires=["nipype"],
)
