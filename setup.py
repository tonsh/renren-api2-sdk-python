#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="renren_client",
    version="0.0.1",
    keywords=('Renren', 'Oauth2', 'Renren API'),
    description="The renren API2.0 SDK for python",
    long_description="See https://github.com/tonsh/renren-api2-sdk-python",
    license="BSD License",

    author="tonsh",
    author_email="tonshlee@gmail.com",
    url="https://github.com/tonsh/renren-api2-sdk-python",

    packages=find_packages(exclude=["tests.*", "example.*", "examples"]),
    include_package_data=True,
    platforms='any',
    zip_safe=False,
)
