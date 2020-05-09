#!/usr/bin/env python3

import os
import re
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'src', 'celeref_lang', 'version.py')) as fp:
    VERSION = re.match(r'^VERSION = \'(.*?)\'', fp.read(), re.S).group(1)

with open('README.md', 'r', encoding='utf-8') as fp:
    README = fp.read()

with open('requirements.txt', 'r', encoding='utf-8') as fp:
    REQUIREMENTS = [
        line.strip() for line in fp.readlines()
        if line.strip() and not line.startswith('#')
    ]

setup(
    name='celeref-lang',
    version=VERSION,

    # installed or upgraded on the target machine
    install_requires=REQUIREMENTS,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        'celeref_lang': ['schema/*.json']
    },
    entry_points={
        "console_scripts": [
            "celeref = celeref_lang.main:main",
        ]
    },

    # metadata to display on PyPI
    author='Sudipto Chandra',
    author_email='dipu.sudipta@gmail.com',
    url='https://github.com/dipu-bd/celeref-lang',
    description='A interpreter for celeref programming language',
    keywords='interpreter language celeref',
    long_description_content_type='text/markdown',
    long_description=README,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Free For Educational Use',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
