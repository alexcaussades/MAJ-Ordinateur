import os
import platform
import re
import requests
import sys
import winreg
import json
import time

# Recherche des Mise à jour des programmes via winget 
def update():
    print("Mise à jour des programmes via winget")
    return os.system("winget upgrade")

# Mise à jour de tous les programmes via winget
def update_all():
    print("Mise à jour de tous les programmes via winget")
    return os.system("winget upgrade --all -h -e")

# Export des programmes installés via winget
def export():
    print("Export des programmes installés via winget")
    return os.system("winget export --output winget_Export.json")

# Verification de l'export des programmes via winget
def verify_export():
    print("Verification de l'export des programmes via winget")
    time.sleep(10)
    try:
        with open('winget_Export.json') as json_file:
            data = json.load(json_file)
            print("Export winget effectué")
    except:
        print("Export winget non effectué")

# Import des programmes installés via winget
def import_logiciel():
    print("Import des programmes installés via winget")
    return os.system("winget import winget_Export.json")

# installation de winget sur le systeme
def install_winget():
    print("Installation de winget sur le systeme")
    return os.system("pip install winget-cli")

# verification de l'installation de winget sur le systeme

def verify_install_winget():
    print("Verification de l'installation de winget sur le systeme")
    time.sleep(2)
    try:
        os.system("winget --version")
    except:
        print("Winget non installé")
        install_winget()
        print("Winget installé")