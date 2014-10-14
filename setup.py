#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Click',
    'six',
    'pyyaml',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='planemo',
    version='0.0.1',
    description='Command-line utilities to assist in building tools for the Galaxy project (http://galaxyproject.org/).',
    long_description=readme + '\n\n' + history,
    author='Galaxy Project and Community',
    author_email='jmchilton@gmail.com',
    url='https://github.com/jmchilton/planemo',
    packages=[
        'planemo',
        'planemo.commands',
        'galaxy',
        'galaxy.tools',
        'galaxy.tools.linters',
        'galaxy.tools.deps',
        'galaxy.tools.deps.resolvers',
        'galaxy.util',
    ],
    entry_points='''
        [console_scripts]
        planemo=planemo.cli:planemo
    ''',
    package_dir={'planemo': 'planemo',
                 'galaxy': 'galaxy'},
    include_package_data=True,
    install_requires=requirements,
    license="AFL",
    zip_safe=False,
    keywords='planemo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
