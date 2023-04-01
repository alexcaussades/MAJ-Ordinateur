
import os
import sys
import requests
import modules.winget as winget
import modules.info_pc as info_pc
import datetime as dt



def info():
    print("Inforomation the computer")
    print("the current date", dt.datetime.now())
    print("Go de RAM disponible: " + info_pc.get_available_ram())
    print("Vote processeur: " + info_pc.get_processor_name())
    exit()

def upgrade():
    print("Recherche des mise à jour des programmes via winget")
    winget.update()
    exit()
    
def upgrade_all():
    print("Recherche des mise à jour de tous les programmes via winget")
    winget.upgrate_all()
    exit()

def verify_install_winget():
    print("Verification de l'installation de winget")
    winget.verify_install_winget()
    exit()
    
def install_system():
    print("Installation des dependances du systeme")
    os.system("pip install requests")
    os.system("pip install psutil")
    os.system("winget install git.git -h -e")
    print("Installation des dependances du systeme terminé")
    exit()
    
def help():
    print(" info : Affiche les informations du pc")
    print(" update : Recherche des mise à jour des programmes via winget")
    print(" upgrade : Mise à jour de tous les programmes via winget")
    print(" verify_install_winget : Verification de l'installation de winget")
    exit()