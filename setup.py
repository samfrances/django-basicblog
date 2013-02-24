from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "Django Basic Blog", # Check other projects to see if name is same as package
    version = "0.1",
    packages = find_packages(),
)
