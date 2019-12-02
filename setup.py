from setuptools import setup, find_packages

setup(
    name="arborlife",
    version="0.1.0",
    description="Python implementation of Arbor Life simulation.",
    url="https://github.com/rogerhurwitz/arborlife",
    author="Roger Hurwitz",
    author_email="rogerhurwitz@gmail.com",
    install_requires=[
        "mpmath",
        "PyYAML",
    ],
    data_files=[
        ("config", [
            "tree.yaml",
        ])
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
)
