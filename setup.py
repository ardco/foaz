from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in foaz/__init__.py
from foaz import __version__ as version

setup(
	name="foaz",
	version=version,
	description="HR",
	author="Mai Ismail",
	author_email="mai.mq.1995@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
