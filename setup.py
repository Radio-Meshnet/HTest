###########################################################################################
#
# ĦTest
#
# Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License
#
###########################################################################################


#### Import ####
import os
import re
import setuptools
from pathlib import Path


#### Get Var ####
def get_var(file, var) -> str:
    content = open(file, "rt", encoding="utf-8").read()
    try:
        regex = r"(?<=^"+var+" = ['\"])[^'\"]+(?=['\"]$)"
        value = re.findall(regex, content, re.M)[0]
        return value
    except IndexError:
        raise ValueError(f"Unable to find string {var} in {file}.")
        return ""


#### Build ####
with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = os.path.join(os.path.dirname(__file__), "htest", "main.py")

package_data = {
"": [
    "assets/*",
    ]
}

print("Packaging "+get_var(version_file, "__title__")+" "+get_var(version_file, "__version__")+" "+get_var(version_file, "__version_variant__"))

setuptools.setup(
    name=get_var(version_file, "__package_name__"),
    version=get_var(version_file, "__version__"),
    author=get_var(version_file, "__author__"),
    author_email=get_var(version_file, "__author_email__"),
    description=get_var(version_file, "__description__"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=get_var(version_file, "__copyright_url__"),
    packages=setuptools.find_packages(),
    package_data=package_data,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    entry_points= {
        'console_scripts': [
             get_var(version_file, "__package_name__")+'=htest.main:main',
        ]
    },
    install_requires=[""],
    extras_require={
        "macos": ["pyobjus"],
    },
    python_requires=">=3.6",
)
