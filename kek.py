import colorama
import random
from colorama import init,Fore

cat = """.                                                                         /\_/\           ___
.                                                                        = o_o =_______    \ \  
.                                                                         __^      __(  \.__) )
.                                                                     (@)<_____>__(_____)____/"""

init(autoreset=True)
bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_chars = [random.choice(colors) + char for char in cat]
print(''.join(colored_chars))