import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '1.0'

REPO_NAME = 'Kidney-disease-classification'
author = 'Satyanarayan'
src_repo = 'cnnClassifier'

setuptools.setup(
    name=src_repo,
    version=__version__,
    author= author,
    url=f'https://github.com/satyanarayansenapati/Kidney-disease-classification.git'

)