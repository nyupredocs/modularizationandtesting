import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OLS_team_cool", # Replace with your own username
    version="0.0.1",
    author="Team Cool",
    author_email="gen.li@yale.edu",
    description="A small example package for OLS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        'NYU Predoctoral repo': 'https://github.com/nyupredocs'
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
