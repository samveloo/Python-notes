import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

text = input("Enter text: ")
art = pyfiglet.figlet_format(text)

print(Fore.BLUE + art)