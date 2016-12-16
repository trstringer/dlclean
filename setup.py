"""Setup for dlclean"""

from setuptools import setup

setup(
    name='dlclean',
    version='0.1.0',
    packages=['dlclean'],
    entry_points={
        'console_scripts': [
            'dlclean = dlclean.__main__:main'
        ]
    }
)
