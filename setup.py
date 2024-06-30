# setup.py

from setuptools import setup, find_packages

setup(
    name='data_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'chardet'
    ],
)
