from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME = "insurance-premium-predictor"
VERSION = "0.0.1"
AUTHOR= "Bhawna Saini"
DESCRIPTION="This project is going to predict who are the people which may take the insurance in the future based on the various parameters "
PACKAGES = ["Insurance"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention
    in requirements.txt file
    return this function is going to return a list which 
    contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
         return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = PACKAGES,
install_requires = get_requirements_list()

)

if __name__ == "__main__":
    print(get_requirements_list())


