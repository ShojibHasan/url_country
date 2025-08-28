#!/usr/bin/env python3
"""
Setup script for url_country package
"""

import os

from setuptools import find_packages, setup


# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="url_country",
    version="1.0.0",
    author="Mahfujul Hasan",
    author_email="shojibhasan15@gmail.com",
    description="A Python package to determine the country of a URL/domain using multiple methods",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShojibHasan/url_country",
    project_urls={
        "Bug Reports": "https://github.com/ShojibHasan/url_country/issues",
        "Source": "https://github.com/ShojibHasan/url_country",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        "url_country": ["*.mmdb"],
    },
    zip_safe=False,
    keywords="url, domain, country, geolocation, whois, dns, geoip",
)
