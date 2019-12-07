from setuptools import setup, find_packages
import os

#-Write Versions File-#
# Major-Minor-Patch (release-status)
VERSION = '0.0.1'

#-Meta Information-#
#~~~~~~~~~~~~~~~~~~#

DESCRIPTION = "Practice modeling package for NYU predocs program."

LONG_DESCRIPTION = """
Practice modeling package for NYU predocs program. 

Contains OLS and logistic regression model.
"""

LICENSE = 'MIT'

#-Setup-#
#~~~~~~~#

setup(
    name='the_package',
    packages=find_packages(),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    author='Group3',
    project_urls={
        'NYU Predoctoral repo': 'https://github.com/nyupredocs'
    },
    install_requires=[
        'numpy',
		'pandas',
		'scipy'
    ],
    include_package_data=True
)

