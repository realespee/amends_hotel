from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amends_hotel/__init__.py
from amends_hotel import __version__ as version

setup(
	name="amends_hotel",
	version=version,
	description="Hotel Booking",
	author="Simon Wanyama",
	author_email="wanyamasp@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
