import time, os, platform
from colorama import init, Fore
import colorama

logo = """
  _____      _                      ____             
 | ____|_  _| |_ _ __ ___ _ __ ___ |  _ \  _____   __
 |  _| \ \/ / __| '__/ _ \ '_ ` _ \| | | |/ _ \ \ / /
 | |___ >  <| |_| | |  __/ | | | | | |_| |  __/\ V / 
 |_____/_/\_\\__|_|  \___|_| |_| |_|____/ \___| \_/  
                                                     
"""

def clear(): os.system('clear') if not platform.platform().startswith('Windows') else os.system('cls')
def logos(): init();print(Fore.RED + str(logo) + Fore.WHITE, end='\n')
def change_screen(title="New Title"): os.system('title {}'.format(str(title))) if platform.platform().startswith('Windows') else ...