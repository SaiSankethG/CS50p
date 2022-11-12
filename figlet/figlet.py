from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if sys.argv==0:
    user_input=print("Input:")
    rand=figlet.getFonts()
    output=random.choice(rand)
    print(figlet.renderText(user_input))
elif sys.argv==2:
    font_style=sys.argv[1]
    if font_style[0:1]==-f or font_style[0:1]=--:
        
