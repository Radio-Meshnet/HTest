# ĦTest

ĦTest ist ein Tool zum Prüfen und Testen des iop-python-Moduls für die Verwendung des Hydraledger SDK für Python-Anwendungen.


Eine vollständige Dokumentation zu diesem Modul finden Sie unter den folgenden Links:
- https://pypi.org/project/iop-python/
- https://github.com/BukiOffor/hydra-python-api


Alle Informationen über die Hydraledger-Blockchain finden Sie unter den folgenden Links:
- https://www.hydraledger.tech/
- https://github.com/Internet-of-People


## Aktueller Status
Es handelt sich derzeit um eine Betasoftware, die noch in Arbeit ist.

Alle Kernfunktionen sind implementiert und funktionieren, aber Ergänzungen werden wahrscheinlich auftreten, wenn die reale Nutzung erforscht wird.

Es kann zu Fehlern kommen oder die Kompatibilität nach einem Update ist nicht mehr gewährleistet.


## Installation

### Android
- Erstellen Sie die APK mit Buildozer.
- Kopieren Sie die APK auf Ihr Gerät und erlauben Sie die Installation.


### Linux
- Installieren Sie alle erforderlichen Komponenten.
  ```
  pip install -r requirements.txt
  ```
- Installieren Sie die iop-python- Voraussetzungen.
  ```
  sudo apt install curl
  sudo apt install pkg-config
  sudo apt install libssl-dev
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  . "$HOME/.cargo/env"
  pip3 install maturin
  pip3 install iop-python
  ```
- Starten Sie die App mit `python main.py`.


# Copyright

Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License