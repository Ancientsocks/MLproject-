from setuptools import find_packages , setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    ...

    

    ...
    requirments = []
    with open(requirements.txt) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]



setup(
    name = 'MLproject' , 
    version = '0.0.1' ,
    author = 'Abdul' ,
    author_email = 'Rahaman188370@gmail.com' ,
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt')

)