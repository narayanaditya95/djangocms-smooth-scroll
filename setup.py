#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_wow import __version__


INSTALL_REQUIRES = [
    'django-cms>=3.0',
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name='djangocms-scroll-smooth',
    version=__version__,
    description='',
    author='Sourish Ghosh',
    author_email='ragnarok0211@gmail.com',
    url='https://github.com/sourishg/djangocms-wow',
    packages=['djangocms_scroll_smooth', 'djangocms_scroll_smooth.migrations', 'djangocms_scroll_smooth.south_migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read() + open('CHANGELOG.rst').read(),
    include_package_data=True,
    keywords='django cms smooth scroll',
    zip_safe=False,
    test_suite='test_settings.run',
)
