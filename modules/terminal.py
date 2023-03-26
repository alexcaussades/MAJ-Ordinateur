import requests
import os
import platform
import re
import winreg

# Installation automatique du nouveau terminal (si besoin) via les commandes suivantes : avec ULR https://github.com/microsoft/terminal/releases

def new_terminal():
    # determine if windows 
    win_versionSystem = platform.release()
    # Installation du nouveau terminal
    r = requests.get('https://api.github.com/repos/microsoft/terminal/releases/latest')
    
    for asset in r.json().get('assets'):
        if asset.get('name').endswith('.msixbundle'):
            # regex sur le nom du fichier pour récupérer la version avec Win 10 ou 11
            version = re.search(r'(?<=Microsoft.WindowsTerminal_)(.*)(?=.msixbundle)', asset.get('name'))
            f = version.group(0).split('_')
            if f[0] == 'Win'+win_versionSystem:
                # recuperation de l'url du fichier
                url = asset.get('browser_download_url')
                print(url)
                # telechargement du fichier
                r = requests.get(url, allow_redirects=True)
                # enregistrement du fichier
                t = open('Microsoft.WindowsTerminal_'+f[0]+'_'+f[1]+'.msixbundle', 'wb').write(r.content)
                # voir si le fichier est bien enregistré
                t = os.system('dir Microsoft.WindowsTerminal_'+f[0]+'_'+f[1]+'.msixbundle')
                # installation du fichier
                t = os.system('start Microsoft.WindowsTerminal_'+f[0]+'_'+f[1]+'.msixbundle')
                # suppression du fichier
                t = os.system('del Microsoft.WindowsTerminal_'+f[0]+'_'+f[1]+'.msixbundle')


def Get_Version_Terminal_Windows():
    # determeine la derniere version du terminal windows
    try:
        # Open Windows Terminal key
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        reg_key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\wt.exe")
        # Get version value on Windows Terminal key "C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.16.10262.0_x64__8wekyb3d8bbwe\wt.exe"
        version = winreg.QueryValueEx(reg_key, "Path")[0]
        # regex sur le nom du fichier pour récupérer la version avec Win 10 ou 11
        version2 = re.search(r'(?<=Microsoft.WindowsTerminal_)(.*)(?=_x)', version)
        r = requests.get('https://api.github.com/repos/microsoft/terminal/releases/latest')
        r.json().get('tag_name')
        # compare les deux versions
        if r.json().get('tag_name') <= "v"+version2.group(0):
            print("La version du terminal windows est à jour")
        else:
            print("La version du terminal windows n'est pas à jour")
            new_terminal()
    except Exception as e:
        print(f"Error: {e}") 
    

def Utlisateurs():
    os.system('net user > users.txt') 

if __name__ == "__main__":
    Get_Version_Terminal_Windows()