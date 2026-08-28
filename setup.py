# setup.py
from setuptools import setup, find_packages

setup(
    name='dataextractor',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dataextractor=main:main',
        ],
    },
)
