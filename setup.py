from setuptools import setup, find_packages

version = {}
with open('arborlife/version.py') as fp:
    exec(fp.read(), version)

setup(
    name="arborlife",
    version=version["__version__"],
    description="Python implementation of Arbor Life simulation.",
    url="https://github.com/rogerhurwitz/arborlife",
    author="Roger Hurwitz",
    author_email="rogerhurwitz@gmail.com",
    install_requires=[
        "PyYAML", "numpy", "scipy",
    ],
    package_data={'arborlife': ['config/*.yml']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
)
