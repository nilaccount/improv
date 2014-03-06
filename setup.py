#! ../env/bin/python

import os
import sys
import improv

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

README = open('README.rst').read()
LICENSE = open("LICENSE").read()

setup(
    name='improv',
    version=improv.__version__,
    description='You learn by doing. You can\'t improve what you don\'t measure',
    long_description=(README),
    license=LICENSE,
    author='Nil',
    author_email='nonilexit@gmail.com',
    url='http://github.com/nilaccount/improv',
    install_requires=[''],
    packages=[],
    include_package_data=True,
    scripts=[''],
    classifiers=(
        'Development Status :: Development',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    keywords='python, git, guidelines',
    tests_require=['nose'],
    test_suite='tests',
)
