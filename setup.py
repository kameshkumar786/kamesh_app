from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kamesh_app/__init__.py
from kamesh_app import __version__ as version

setup(
	name="kamesh_app",
	version=version,
	description="Description of kamesh app",
	author="kamesh kumar",
	author_email="kamesh3928@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
