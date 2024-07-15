import setuptools
from setuptools import find_packages, setup
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-To-End-ML-Project-MLflow-AWS"
SRC_REPO = "mlProject"
AUTHOR_NAME = "Raja Marthala"
AUTHOR_EMAIL = "marthalarajavardhanreddy@gmail.com"
AUTHOR_USER_NAME = "vardhan9"
HYPEN_E_DOT='-e .'
#this function returns a list of requirements
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: 
        requirements=file_obj.readlines() #reading requirements files line by line
        requirements= [req.replace("\n","") for req in requirements] #reading next line add \n, so here we are replacing with " "
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for ML app",
    long_description=long_description,
    url="http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "SRC"},
    packages = setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)