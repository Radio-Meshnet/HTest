###########################################################################################
#
# ĦTest
#
# Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License
#
###########################################################################################


#### Import ####
import sys
import os
import re
from pathlib import Path

import pyinstaller_versionfile
#from kivy_deps import sdl2, glew
#from kivymd import hooks_path as kivymd_hooks_path


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
path = os.path.abspath(".")

version_file = "main.py"
main_file = "main.py"

pyinstaller_versionfile.create_versionfile(
    output_file="version.rc",
    version=get_var(version_file, "__version__")+".0",
    company_name=get_var(version_file, "__author__"),
    file_description=get_var(version_file, "__description__"),
    internal_name=get_var(version_file, "__title__"),
    legal_copyright=get_var(version_file, "__copyright_short__"),
    original_filename=get_var(version_file, "__title__")+".exe",
    product_name=get_var(version_file, "__title__")
)

added_files = [
    ("assets/esptool.exe", "assets"),
    ("assets_firmware", "assets_firmware"),
]

a = Analysis(
    [main_file],
    pathex=[path],
    #hiddenimports=["plyer.platforms.win.storagepath"],
    #hookspath=[kivymd_hooks_path],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
    datas=added_files,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    #*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name=get_var(version_file, "__package_name__")+"-"+get_var(version_file, "__version__"),
    icon="assets\icon.ico",
    console=True,
    version="version.rc",
)