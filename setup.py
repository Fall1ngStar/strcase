import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strcase",
    version="0.0.3",
    author="Fall1ngStar",
    description="Convert string to specific case",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fall1ngStar/strcase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)