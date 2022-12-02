from importlib import reload
import socket
import pyfiglet
import colorama
from colorama import *
import os

colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
ascii_banner = pyfiglet.figlet_format("PieSpy")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)


hostname = input("Enter target domain (e.g reddit.com):\n")


#IP lookup from hostname
print(f'\nIP Address for {hostname} is {socket.gethostbyname(hostname)}')

back=input(Fore.RED + "\nPress to Exit" + Style.RESET_ALL)
