import sys
from pyfiglet import Figlet

figlet=Figlet()
if len(sys.argv)==1:
    random=True
elif len(sys.argv)==3:
    random=False
else:
    sys.exit()

msg=input("Input:")
figlet.getFonts()
if random==False:
    try:
        figlet.setFont(f=sys.argv[2])
        print(figlet.renderText(msg))
    except :




