import setuptools
from setuptools import setup, find_packages

with open('README.md','r',encoding="utf-8") as fh:
    long_descriotion =  fh.read()

setup(
    name='terminal_progress_bar',
    version='0.1',
    author="Aly Abdelaal",
    author_email="alialsayedali.aa@gmail.com",
    description="Print Progress Bar in terminal, cmd, PowerShell, etc...",
    long_description=long_descriotion,
    packages=find_packages(where="src"),
    requires=[],
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"        
    ]

)