from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if sys.argv==0:
    user_input=print("Input:")
    rand=figlet.getFonts()
    output=random.choice(rand)
    print(figlet.renderText(user_input , font=rand))
elif sys.argv==2:
    font_type=sys.argv[1]
    font_style=sys.argv[2]
    if font_type[0:1]=="-f" or font_type[0:]=="--font":
        user_input:print("Input:")
        print(figlet.renderText(user_input, font=font_style))
    else:
        sys.exit()

