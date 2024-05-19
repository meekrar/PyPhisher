#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='PyPhisher',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='meekrar',
    author_email='hackermeekrar@gmail.com',
    license="MIT",
    url='https://github.com/meekrar/PyPhisher/',
    scripts=['pyphisher'],
    install_requires=["requests", "rich"]
)
