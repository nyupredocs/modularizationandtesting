from setuptools import setup, find_packages
import os

#-Write Versions File-#
# Major-Minor-Patch (release-status)
VERSION = '0.0.1'

def write_version_py(filename=None):
    """
    This constructs a version file for the project
    """
    doc = "\"\"\"\nThis is a VERSION file and should NOT be manually altered\n\"\"\""
    doc += "\nversion = '%s'\n" % VERSION

    if not filename:
        filename = os.path.join(os.path.dirname(__file__), 'transcripty', 'version.py')

    fl = open(filename, 'w')
    try:
        fl.write(doc)
    finally:
        fl.close()

# This is a file used to control the transcripty.__version__ attribute
write_version_py()

#-Meta Information-#
#~~~~~~~~~~~~~~~~~~#

DESCRIPTION = "Practice modeling package for NYU predocs program. "

LONG_DESCRIPTION = """
Practice modeling package for NYU predocs program. 

Contains OLS and logistic regression model.
"""

LICENSE = 'MIT'

#-Setup-#
#~~~~~~~#

setup(
    name='transcripty',
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
		'scipy',
		'unittest',
		'rando'
    ],
    include_package_data=True
)

