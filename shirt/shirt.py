import sys
from PIL import image
def main():
    validate()
    try:
        

def validate():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".") != sys.argv[2].split("."):
        sys.exit("Input and output have different extensions")
