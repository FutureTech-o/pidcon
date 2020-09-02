from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy==1.19.1"]

setup(
    name="pidcon",
    version="0.0.2",
    author="Akram Abu Owaimer",
    author_email="Akram.AbuOwaimer@gmail.com",
    description="A package to handle simple PID controller",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/FutureTech-o/pidcon",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
