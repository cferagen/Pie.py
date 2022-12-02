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
                message="Select Hash Verification Method",
                choices=['MD5', 'SHA256'],
            ),
]
select = inquirer.prompt(questions)


if select['hashoption'] == "MD5":
	import verifyhashmd5
if select['hashoption'] == "SHA256":
	import verifyhashsha256
