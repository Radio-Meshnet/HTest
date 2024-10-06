# ĦTest

ĦTest is a tool for checking and testing the iop-python module for using the Hydraledger SDK for Python applications.


A complete documentation about this module can be found on the following links:
- https://pypi.org/project/iop-python/
- https://github.com/BukiOffor/hydra-python-api


All information about the Hydraledger blockchain can be found on the following links:
- https://www.hydraledger.tech/
- https://github.com/Internet-of-People


## Current status
This is currently beta software that is still a work in progress.

All core features are implemented and working, but additions will likely occur as real-world usage is explored.

Bugs may occur or compatibility may not be guaranteed after an update.


## Installation

### Android
- Build the APK with buildozer.
- Copy the APK to youre device and allow the installation.


### Linux
- Install all requirements.
  ```
  pip install -r requirements.txt
  ```
- Install iop-python requirements.
  ```
  sudo apt install curl
  sudo apt install pkg-config
  sudo apt install libssl-dev
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  . "$HOME/.cargo/env"
  pip3 install maturin
  pip3 install iop-python
  ```
- Start the app with `python main.py`.


# Copyright

Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License