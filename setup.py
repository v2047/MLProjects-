from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [
            req.strip() for req in file_obj.readlines() if req.strip() and not req.startswith("#")
        ]
        # Remove '-e .' since it is not valid in install_requires
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="MLproject",
    version='0.0.1',
    author='Vanshika',
    author_email='tomar9231@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
