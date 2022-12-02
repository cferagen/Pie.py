import hashlib
import os
import pyfiglet
import colorama
from colorama import *
colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

ascii_banner = pyfiglet.figlet_format("Pie Hash SHA256")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# File to check
file_name = input("Enter file path:\n")

# Correct original md5 goes here
original_sha256 = input("\nEnter original SHA256 Hash:\n")  

# Open,close, read file and calculate MD5 on its contents 
with open(file_name, 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    sha256_returned = hashlib.sha256(data).hexdigest()

# Finally compare original MD5 with freshly calculated
if original_sha256 == sha256_returned:
    print(Fore.GREEN + "\nSHA256 verified\n" + Fore.RESET)
else:
    print(Fore.RED + "\nSHA256 verification failed\n" + Fore.RESET)

back=input(Fore.RED + "\nPress to Exit" + Style.RESET_ALL)
