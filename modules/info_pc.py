import psutil
import platform
import os
import datetime as dt
import subprocess


def get_available_ram():
    # Get the amount of available RAM in bytes
    available_ram = psutil.virtual_memory().available
    # Convert bytes to gigabytes
    available_ram_gb = available_ram / (1024**3)
    f = "{:.0f}".format(available_ram_gb)
    return f


def get_processor_name():
    # Get the processor name
    processor_name = platform.processor()
    return processor_name


# regedit sauvegarde en totalité


def save_regedit():
    # Sauvegarde du regedit
    os.system("regedit /e C:\Windows\Temp\regedit.reg HKEY_CURRENT_USER")


if __name__ == "__main__":
    print("the current date and time is", dt.datetime.now())
    print("Go de RAM disponible: " + get_available_ram())
    print("Vote processeur: " + get_processor_name())
