import hashlib
import os
import pyfiglet
import colorama
import inquirer
from colorama import *
colorama.init()

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
ascii_banner = pyfiglet.figlet_format("Pie IP")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# Options
questions = [
  inquirer.List('ipoption',
                message="Select IP Tool",
                choices=['NSLookup', 'Port Scan'],
            ),
]
select = inquirer.prompt(questions)


if select['ipoption'] == "NSLookup":
	import nslookup
if select['ipoption'] == "Port Scan":
	import portscan

