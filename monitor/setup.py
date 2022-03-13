#!/usr/bin/env python                                                                                                                                        
from setuptools import setup, find_packages

# https://www.tutorialguruji.com/python/python-package-structure-setup-py-for-running-unit-tests/
# this is allows to run test in seperate folder
# via this script
# for single test class
# -s <fully qualified test module>
# to clean cruft : py3clean .
setup(version='0.1',
      description='honeyPi beehive montiro',
      author='tim Cronin',
      author_email='tecronin@gmail.com',
      packages=find_packages(),
      install_requires=[],
      test_suite="tests",                          
)