from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="honeydesk"
DESCRIPTION="This is a first Machine Learning Project"
# PACKAGES = 'housing'

REQUIREMENT_FILE_NAME="requirements.txt"

# def get_requirements_list()->List[str]:           
#    pass

def get_requirements_list()->List[str]:
    """
   
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return: This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove ("-e .")  


# setup() is a function like a pre-build function.
# passing values to the different parameters of the function.
setup(
name="PROJECT_NAME",
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
# or packages=PACKAGES          => # instead of this, above we have called find_packages() 
                                   # to detect packages from the code                         
install_requires=get_requirements_list()
)
