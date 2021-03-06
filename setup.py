# noinspection SpellCheckingInspection
__author__ = 'wookjae.jo'

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonut",
    version="0.1.0",
    author="wookjae.jo",
    author_email="jwj0104@gmail.com",
    description="JSON Dataclass Object Mapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/positive-man/jsonut",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
