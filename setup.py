from os import path

from setuptools import find_packages, setup

version = {}
with open('arborlife/version.py') as fp:
    exec(fp.read(), version)

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="arborlife",
    version=version["__version__"],
    description="An open source forest-centric simulation library.",
    long_description=long_description,
    url="https://github.com/rogerhurwitz/arborlife",
    author="Roger Hurwitz",
    author_email="rogerhurwitz@gmail.com",
    install_requires=[
        "PyYAML>=5.2",
        "numpy>=1.17.4",
        "scipy>=1.3.3",
    ],
    package_data={'arborlife': ['config/*.yml']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs')),
)
