#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup

from graphensemble import __version__


REQUIREMENTS_FILE = 'requirements.txt'
DEV_REQUIREMENTS_FILE = 'dev-requirements.txt'


dev_requirements = open(
        os.path.join(os.path.dirname(__file__), DEV_REQUIREMENTS_FILE)).read().split()
requirements = open(
        os.path.join(os.path.dirname(__file__), REQUIREMENTS_FILE)).read().split()

setup(
    name='graphensemble', 
    license='BSD',
    version=__version__,
    description='Assemble Structured Data from Graph Nodes',
    author='Cindy Cao',
    author_email='cindy@candidnarrative.com',
    url='http://github.com/cindyc/graphensemble',
    packages=['graphensemble',],
    install_requires=requirements,
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
