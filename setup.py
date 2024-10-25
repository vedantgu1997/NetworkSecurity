from setuptools import setup, find_packages
from typing import List

def get_requirements():
    'This function returns a list of requirements from the requirements.txt file'
    req_list = []
    try:
        with open('requirements.txt') as f:
            lines = f.readlines()
            #Processing the lines
            for line in lines:
                requirement = line.strip()
                #ignoring empty lines and -e .
                if requirement and requirement != '-e .' :
                    req_list.append(requirement)
    
    except FileNotFoundError:
        print('requirements.txt file not found')

    return req_list

setup(
    name = 'NetworkSecurity',
    version = '0.0.0.1',
    author = 'Vedant Gupta',
    packages = find_packages(),
    install_requires = get_requirements()
)