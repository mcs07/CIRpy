#!/usr/bin/env python

import os
from setuptools import setup


if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''CIRpy is a Python interface for the Chemical Identifier Resolver web service that is provided
by the CADD Group at the NCI/NIH.'''

setup(
    name='CIRpy',
    version='1.0.1',
    author='Matt Swain',
    author_email='m.swain@me.com',
    license='MIT',
    url='https://github.com/mcs07/CIRpy',
    py_modules=['cirpy'],
    description='Python wrapper for the NCI Chemical Identifier Resolver (CIR).',
    long_description=long_description,
    keywords='python rest api chemistry cheminformatics',
    extras_require={'lxml': ['lxml']},
    test_suite='cirpy_test',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
