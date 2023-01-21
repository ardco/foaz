# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in fouz/__init__.py
from fouz import __version__ as version

setup(
	name='fouz',
	version=version,
	description='hr structer ',
	author='ARD',
	author_email='Hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
