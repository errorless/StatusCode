# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='StatusCode',
    version=version,
    keywords='StatusCode',
    description='Python Status Code based on ``kkconst``',
    long_description=open('README.rst').read(),

    url='https://github.com/errorless/StatusCode',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['StatusCode'],
    py_modules=[],
    install_requires=['kkconst'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
