import os

from setuptools import setup, find_packages
from pathlib import Path
from typing import List

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

PROJECT_NAME = "neuro_mf"
VERSION = "0.0.5"
AUTHOR = "Avnish Yadav"
DESCRIPTION = """
   iNeuron Model Factory helps us to generate model training and grid search code automatically based 
    on configuration provided.
    """
REPO_NAME = "model_factory"
AUTHOR_USER_NAME  = "avnyadav"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["PyYAML","scikit-learn"],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
)
