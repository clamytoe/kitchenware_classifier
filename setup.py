"""
setup.py

Setup for installing the package.
"""
from pathlib import Path

from setuptools import find_packages, setup

import kitchenware_classifier

VERSION = kitchenware_classifier.__version__
AUTHOR = kitchenware_classifier.__author__
EMAIL = kitchenware_classifier.__email__

BASE_DIR = Path(__file__).resolve().parent
README = BASE_DIR.joinpath("README.md")

setup(
    name="kitchenware_classifier",
    version=VERSION,
    description="Classifies kitchen stuff items into 6 categories: cups, glasses, plates, spoons, forks and knives (kitchenware_classifier)",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/clamytoe/kitchenware_classifier",
    author=AUTHOR,
    author_email=EMAIL,
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9.13",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pytest"],
    license="MIT",
    entry_points={
        "console_scripts": ["kc=kitchenware_classifier.app:main"],
    },
    project_urls={
        "Bug Reports": "https://github.com/clamytoe/kitchenware_classifier/issues",
        "Source": "https://github.com/clamytoe/kitchenware_classifier/",
    },
)
