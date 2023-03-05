from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    libs = []
    with open(filepath, 'r') as f:
        r = f.readlines()
        r = [req.replace("\n", "") for req in r]
        
    if HYPHEN_E_DOT in r:
        r.remove(HYPHEN_E_DOT)

    return r

   

get_requirements('requirements.txt')

setup(
    name="MLProject",
    version="0.0.1",
    author="Hemil",
    author_email="hemilparmar1005@gmail.com",
    requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )