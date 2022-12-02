import hashlib
import os
import pyfiglet
import colorama
from colorama import *
colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
ascii_banner = pyfiglet.figlet_format("Pie Hash")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# File to check
file_name = input("Enter file path:\n")

# Open,close, read file and calculate MD5 on its contents 
with open(file_name, 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()

with open(file_name, 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    sha256_returned = hashlib.sha256(data).hexdigest()

print(Fore.YELLOW + "\nMD5:\n" + Fore.RESET + md5_returned + "\n")
print(Fore.YELLOW + "SHA256:\n" + Fore.RESET + sha256_returned + "\n")

back=input(Fore.RED + "\nPress to Exit" + Style.RESET_ALL)