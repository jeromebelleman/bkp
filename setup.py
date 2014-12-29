#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='bkp',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Back up files",
    long_description="Back up files and encrypt them on the fly if needs be.",
    scripts=['bkp'],
    data_files=[('share/man/man1', ['bkp.1'])],
)
