#!/usr/bin/env python
"""grpc_python_example

Shows an example of a grpc server that communicates with a Postgres database
using SQLAlchemy as an ORM, and Alembic for migrations.

Also shows example clients including:
    - a RESTful, JSON-API client using Flask
    - a text client using custom classes and Click to provide a cli
"""

import os
import os.path
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

VERSION = '0.1.0'

ROOT = os.path.realpath(os.path.join(os.path.dirname(
    sys.modules['__main__'].__file__)))


def get_requirements(extra='common'):
    """Get requirements for given extra.

    Args:
        extra (str): name of file without extension in requirements/

    Returns:
        (list): list of strings, each formatted as pip install compatible
            requirement specifier.
    """
    file_name = '%s.txt' % extra
    requirements_path = os.path.join(ROOT, 'requirements', file_name)
    pip_reqs = parse_requirements(requirements_path, session='hack')
    reqs = [str(r.req) for r in pip_reqs]
    return reqs


setup(
    name='grpc_python_example',
    version=VERSION,
    author='Michelle D. Zhang',
    author_email='zhang.michelle.d@gmail.com',
    url='',
    description='A grpc python example.',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    packages=find_packages(),
    install_requires=get_requirements(),
    extras_require={
        'dev': get_requirements('dev'),
        'docker': get_requirements('docker'),
        'grpc': get_requirements('grpc'),
        'http': get_requirements('http'),
        'postgres': get_requirements('postgres'),
    },
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development'
    ],
)
