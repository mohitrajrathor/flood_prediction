from setuptools import find_packages, setup 
from typing import List # type: ignore

# constants
HYPEN_E_DOT = "-e ."


# function
def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Flood Prediction",
    version="0.0.1",
    author="Mohit Raj Rathor",
    author_email="mohitrajrathor@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)