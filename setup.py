#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

assert sys.version_info >= (2, 6), 'We only support Python 2.6+'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'asana'))
from version import VERSION

setup(name='asana',
      version=VERSION,
      description='Asana API client',
      # license='',
      install_requires=[
          'requests~=2.9.1',
          'requests_oauthlib~=0.6.1',
          'six~=1.10.0'
      ],
      author='Asana, Inc',
      # author_email='',
      url='http://github.com/asana/python-asana',
      packages = find_packages(),
      keywords= 'asana',
      zip_safe = True,
      test_suite='tests')
