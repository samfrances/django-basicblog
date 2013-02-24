from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "django-basicblog",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['django>=3.3'], # check

    author = 'Sam Frances',
    author_email = 'sam@samfrances.co.uk',
    description = 'A simple blog app for django',
    license = '???', # fill in
    keywords = 'django python blog',
    url = 'http://github.com/samfrances/django-basicblog',
)
