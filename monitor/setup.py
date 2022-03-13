#!/usr/bin/env python
import os
from setuptools import setup, find_packages, Command

# https://stackoverflow.com/questions/3779915/why-does-python-setup-py-sdist-create-unwanted-project-egg-info-in-project-r
# to clean cruft : py3clean .
class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("py3clean .")
        os.system("rm -vrf ./*.egg-info")


# https://www.tutorialguruji.com/python/python-package-structure-setup-py-for-running-unit-tests/
# this is allows to run test in seperate folder
# via this script
# for single test class
# -s <fully qualified test module>
setup(
    version="0.1",
    description="honeyPi beehive montiro",
    author="tim Cronin",
    author_email="tecronin@gmail.com",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    cmdclass={
        "clean": CleanCommand,
    },
)
