#!/usr/bin/env python3

from distutils.core import setup

import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('kutils/')

#print extra_files

setup(name='kutils',
      version='0.5.6', # major.minor.fix
      description='Frequently used functions library for Python By Khalid Grandi (github.com/xaled).',
      author='Khalid Grandi',
      author_email='kh.grandi@gmail.com',
      url='https://github.com/xaled/kutils/',
      packages=['kutils'],
      package_data={'': extra_files},
     )
