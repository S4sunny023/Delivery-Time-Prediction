from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = "Delivery Time Prediction"
VERSION = "0.0.1"
DESCRIPTION = "This is ML project which predict the time for delivery"
AUTHOR_NAME = "Sunny Gupta"
EMAIL = "s4sunny22@gmail.com"

REQUIREMENTS_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."


#open requirements.txt file open and then read
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE) as requirements_file:
        requirement_list = requirements_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list    



setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=EMAIL,
      packages= find_packages(),
      install_requires = get_requirements_list()
    )