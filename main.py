#!/usr/bin/python3
# Importation des modules
import os
import modules.terminal as terminal
import modules.winget as winget
import modules.info_pc as info_pc

# Installations automatique du nouveau terminal (si besoin) via les commandes suivantes :
# Verification de la version du terminal windows debut du script
print("Hello "+ os.getlogin() + " !" )
print("Go de RAM disponible: "+ info_pc.get_available_ram())
print("Vote processeur: "+ info_pc.get_processor_name())



winget.verify_install_winget()
winget.export()
winget.verify_export()
terminal.Utlisateurs()
info_pc.save_regedit()

print("Verification de la version du terminal windows")
terminal.Get_Version_Terminal_Windows()
winget.update()

input("Press Enter to continue...")

a = input("Voulez-vous mettre à jour tous les programmes ? (y/n) ")
if a == "y":
    winget.update_all()
else:
    print("pas de mise à jour")

print("Nettoyage du disque")
os.system("cleanmgr /sageset:n")