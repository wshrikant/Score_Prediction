from setuptools import setup,find_packages
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    with open(file_path) as file_obj:
        rquirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in rquirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='wshrikant2',
author_email='wshrikant2@gmail.com',
packages=find_packages(),
install_requires= get_requirements('Requirements.txt')
)