#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-tastypie',
    version='0.10.0',
    description='A flexible & capable API layer for Django.',
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='http://github.com/toastdriven/django-tastypie/',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'tastypie',
        'tastypie.utils',
        'tastypie.management',
        'tastypie.management.commands',
        'tastypie.migrations',
        'tastypie.contrib',
        'tastypie.contrib.gis',
        'tastypie.contrib.contenttypes',
    ],
    package_data={
        'tastypie': ['templates/tastypie/*'],
    },
    zip_safe=False,
    requires=[
        # 'mimeparse',
        'dateutil(>=1.5, !=2.0)',
    ],
    install_requires=[
        # 'mimeparse',
        'python-dateutil >= 1.5, != 2.0',
    ],
    tests_require=['mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
