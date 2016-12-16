"""Setup for dlclean"""

from setuptools import setup

setup(
    name='dlclean',
    version='0.1.0',
    packages=['dlclean'],
    install_requires=['termcolor'],
    entry_points={
        'console_scripts': [
            'dlclean = dlclean.__main__:main'
        ]
    }
)
