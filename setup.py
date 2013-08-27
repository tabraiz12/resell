#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='resell',
      version='0.1',
      packages=find_packages(),
      package_data={'resell': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'resell': ['bin/*.pyc']},
      scripts=['resell/bin/manage.py'])
