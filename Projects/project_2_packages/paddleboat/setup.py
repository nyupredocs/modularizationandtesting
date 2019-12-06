import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paddleboat2sls", 
    version="0.0.1",
    author="Harriet Jeon, Nadav Tadelis, Casey McQuillan, Joel Becker",
    author_email="joelhbkr@gmail.com",
    description="Practice publishing an econometric python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nyupredocs/modularizationandtesting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)