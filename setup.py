#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-social',
    version='0.2',
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
    requires = [
        'django',
        'django_native_tags (==0.5.3)',
        'redis (==2.4.10)',
    ]
)
