
#Imports
from importlib import reload
import os
import inquirer
import colorama
from colorama import *
import pyfiglet

colorama.init()

#Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

# Pie Banner
print(Style.DIM + Fore.YELLOW +
"""
	          (
	           )
	      __..---..__
	  ,-='  /  |  \  `=-.
	 :--..___________..--;
	  \.,_____________,./ \n
	""" + Style.RESET_ALL)

# Options
questions = [
  inquirer.List('option',
                message="Select Option",
                choices=['IP Tools', 'Robots.txt', 'File Hash', 'Backdoor'],
            ),
]
select = inquirer.prompt(questions)


if select['option'] == "IP Tools":
	import ipui
elif select['option'] == "Robots.txt":
	import robots
elif select['option'] == "File Hash":
	import hashui
elif select['option'] == "Backdoor":
	import backdoorui