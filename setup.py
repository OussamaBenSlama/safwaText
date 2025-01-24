from setuptools import setup, find_packages

setup(
    name="safwaText",
    version="0.1.0",
    description="A Python package for cleaning, normalizing and stemming Arabic text.",
    author="Oussama Ben Slama",
    author_email="hello@ben-slama.tn",
    packages=find_packages(),
    install_requires=[], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)