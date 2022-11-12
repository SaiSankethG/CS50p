import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
if len(sys.argv)==1:
    user_input=print("Input:")
    rand=figlet.getFonts()
    output=random.choice(rand)
    print(figlet.renderText(user_input , font=rand))
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    user_input=print("Input:")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user_input))
else:
    sys.exit()

