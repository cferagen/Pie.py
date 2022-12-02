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
ascii_banner = pyfiglet.figlet_format("Pie Backdoor")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

# Options
questions = [
  inquirer.List('backdooroption',
                message="Select Backdoor Option",
                choices=['Victim', 'Attacker'],
            ),
]
select = inquirer.prompt(questions)


if select['backdooroption'] == "Victim":
	import victim
if select['backdooroption'] == "Attacker":
	import attacker

