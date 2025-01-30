import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
my_fonts = figlet.getFonts()
chosen_font = ""

if len(sys.argv) == 1:
    chosen_font = random.choice(my_fonts)

if (len(sys.argv) == 3) and (sys.argv[2] in my_fonts) and(sys.argv[1] in ['-f', '--font']):
    chosen_font = sys.argv[2]

else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
figlet.setFont(font = chosen_font)
print(figlet.renderText(user_input))