#!/usr/bin/env python3
"""Set up the Python API client for Netdata."""
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as desc:
    long_description = desc.read()

setup(
    name='netdata',
    version='0.2.0',
    description='Python API for interacting with Netdata.',
    long_description=long_description,
    url='https://github.com/home-assistant-ecosystem/python-netdata',
    download_url='https://github.com/home-assistant-ecosystem/python-netdata/releases',
    author='Fabian Affolter',
    author_email='fabian@affolter-engineering.ch',
    license='MIT',
    install_requires=['aiohttp>=3.7.4,<4', 'async_timeout<4'],
    packages=['netdata'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
