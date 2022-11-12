from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if len(sys.argv)==1:
    user_input=print("Input:")
    rand=figlet.getFonts()
    output=random.choice(rand)
    print(figlet.renderText(user_input , font=rand))
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    font_type=sys.argv[1]
    font_style=sys.argv[2]
    user_input:print("Input:")
    print(figlet.renderText(user_input, font=font_style))
else:
    sys.exit()

