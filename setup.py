"""
Copyright (c) 2014 Michael Merickel, John Anderson
All rights reserved.

Redistribution and use in source and binary forms are permitted
provided that the above copyright notice and this paragraph are
duplicated in all such forms and that any documentation,
advertising materials, and other materials related to such
distribution and use acknowledge that the software was developed
by the Pylons organization.  The name of pylons may not be used
to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except:
    README = ''
    CHANGES = ''

requires = [
    'bcrypt',
    'pyramid',
    'zope.interface',
]

testing_extras = ['pytest', 'pytest-cov', 'coverage', 'mock']
docs_extras = ['Sphinx']
sqla_extras = ['sqlalchemy']

setupkw = dict(
    name='horus',
    version='2.0.0',
    description='Pyramid authentication and registration system',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='pyramid authentication',
    author="Michael Merickel, John Anderson",
    author_email="pylons-discuss@googlegroups.com",
    url="http://github.com/pylons/horus",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=testing_extras,
    install_requires=requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
        'sqla': sqla_extras,
    },
)

setup(**setupkw)
