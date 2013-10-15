#!/usr/bin/python

from setuptools import setup, find_packages, Extension

setup(
    name="zmugjson",
    version="0.1.2",
    description="zmugjson a smugmug.com JSON api",
    long_description="A JSON-based api wrapper used to connect to smugmug.com",
    author="Jesus M. Rodriguez",
    author_email="jmrodri@gmail.com",
    url="https://github.com/jmrodri/zmugjson",
    package_dir={
        'zmugjson': '.',
    },
    py_modules=["zmugjson", "config"],
    license="GPLv2",
)
