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
ascii_banner = pyfiglet.figlet_format("Pie Hash")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# Options
questions = [
  inquirer.List('hashoption',
                message="Select Hash Option",
                choices=['Get Hash', 'Verify Hash'],
            ),
]
select = inquirer.prompt(questions)


if select['hashoption'] == "Get Hash":
	import gethash
if select['hashoption'] == "Verify Hash":
	import verifyhash
