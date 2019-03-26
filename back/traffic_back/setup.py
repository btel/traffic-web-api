#!/usr/bin/env python
#coding=utf-8

from setuptools import setup

setup(
    name='traffic-back',
    packages=['traffic_back'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    package_data={
        'static' : ['*']
    }
)

