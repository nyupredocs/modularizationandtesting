import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iv_reg_dnu", # Replace with your own username
    version="0.0.1",
    author="Best Group 2",
    description="Package for Instrumental Variable Estimation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jettpettus/modularizationandtesting",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
