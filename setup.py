# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-friendfeed-zwei',
    version='0.9',
    description="Implementation of FriendFeed's API that caches FriendFeed lifestream data in your local database for fast presentation.",
    author='Mikkel Høgh',
    author_email='mikkel@hoegh.org',
    url = 'http://github.com/mikl/django-friendfeed-zwei',
    packages=['friendfeed'],
)

