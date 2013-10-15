#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="zmugjson",
    version="0.1.2",
    description="zmugjson a smugmug.com JSON api",
    long_description="A JSON-based api wrapper used to connect to smugmug.com",
    author="Jesus M. Rodriguez",
    author_email="jmrodri@gmail.com",
    url="https://github.com/jmrodri/zmugjson",
    license="GPLv2",

    package_dir={
        'zmugjson': 'src/zmugjson',
    },
    packages = find_packages('src'),
    include_package_data = True,
    py_modules=["zmugjson", "config"],
)
