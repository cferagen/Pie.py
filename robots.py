#Imported modules
import pyfiglet
import urllib.request
import io
import os
import colorama
from colorama import *
colorama.init() 

# Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
ascii_banner = pyfiglet.figlet_format("Pie.txt")
print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

url = input(str("Please enter target URL (e.g https://www.reddit.com):\n"))
#Uses URL Library to obtain information on URL's with a robots.txt page.
#Uses IO to format output from request.
def get_robots_txt(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'
	req = urllib.request.urlopen(path + "robots.txt", data=None)
	data = io.TextIOWrapper(req, encoding='utf-8')
	return data.read()

print("\n" + get_robots_txt(url))

back=input(Fore.RED + "\nPress to Exit" + Style.RESET_ALL)