#!/usr/bin/python3
# -*- coding: cp1252 -*-
# Importation des modules
import os
import modules.terminal as terminal
import modules.winget as winget
import modules.info_pc as info_pc
import modules.argument as arg_log
import datetime as dt
import subprocess
import sys


# Installations automatique du nouveau terminal (si besoin) via les commandes suivantes :
# Verification de la version du terminal windows debut du script

# mise en place des arguments
if len(sys.argv) > 1:
    if sys.argv[1] == "info":
        arg_log.info()
    elif sys.argv[1] == "update":
        arg_log.upgrade()
    elif sys.argv[1] == "upgrade":
        arg_log.upgrade_all()
    elif sys.argv[1] == "clean":
        os.system("cleanmgr /sageset:n")
    elif sys.argv[1] == "users":
        terminal.Utlisateurs()
    elif sys.argv[1] == "winget":
        arg_log.verify_install_winget()
    elif sys.argv[1] == "help":
        arg_log.help()
    elif sys.argv[1] == "export":
        winget.verify_export()
    elif sys.argv[1] == "install":
        arg_log.install_system()
    else:
        print("Pas de paramètre")

print('the current date and time is', dt.datetime.now())
print("Hello "+ os.getlogin() + " !" )
print("Go de RAM disponible: "+ info_pc.get_available_ram())
print("Vote processeur: "+ info_pc.get_processor_name())

winget.verify_install_winget()
winget.export()
winget.verify_export()
terminal.Utlisateurs()


print("Verification de la version du terminal windows")
terminal.Get_Version_Terminal_Windows()
winget.update()

input("Press Enter to continue...")

a = input("Voulez-vous mettre à jour tous les programmes ? (yes (y) / no (n)) ")
if a == "y":
    # winget.update_all()
    print("Mise à jour des programmes")
else:
    print("pas de mise à jour")

print("Nettoyage du disque")
os.system("cleanmgr /sageset:n")

    

