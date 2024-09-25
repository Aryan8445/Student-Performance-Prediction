from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file: str) -> list[str]:
    '''
    Read the requirements file and return the list of requirements
    '''
    req=[]
    with open(file) as f:
        req = f.readlines()
        req = [item.replace("\n","") for item in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup(
    name='Student Performance Prediction',
    version='0.1',
    author='Aryan Bhardwaj',
    author_email='aryanbhardwaj3166@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)
