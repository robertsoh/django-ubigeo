#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = '0.1.0'

readme = open('README.rst').read()

setup(
    name='ubigeo',
    version=version,
    description="""A database with Ubigeo codes""",
    long_description=readme,
    url='https://bitbucket.org/minsa-dev/django-ubigeo',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    zip_safe=False,
    keywords='ubigeo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
