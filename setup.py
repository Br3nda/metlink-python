import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='metlinkt',
    version='0.1',
    author="Brenda Wallace",
    author_email="brenda@brenda.nz",
    description="A wrapper for Metlink's API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/br3nda/metlink-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
)