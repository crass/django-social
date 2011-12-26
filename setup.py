#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-subscription',
    version='0.0',
    author='James Pic',
    author_email='jamespic@gmail.com',
    description='Django app with facebook-like features',
    url='http://github.com/yourlabs/django-social',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
