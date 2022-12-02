import socket
import sys
from datetime import datetime
import threading
import os
import pyfiglet
import concurrent.futures
import colorama
from colorama import *
colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

#Enables threading for port scans
print_lock = threading.Lock()

# Banner
ascii_banner = pyfiglet.figlet_format("Pie Scan")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# Input for host IP
ip = input("Enter Host IP to scan:\n")

#Scan is defined by imported module functions.
#Uses sockets to obtain data from the internet.
#Prints out open ports
#Timer set to pass closed ports and move on to the open ports.
print("\nScanning started at: " + str(datetime.now()))
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Open")
    except:
        pass

#Sets the amount of threads to run, and the range for ports. 
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)

back=input(Fore.RED + "\nPress to Exit" + Style.RESET_ALL)