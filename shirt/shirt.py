import sys
from PIL import image
def main():
    validate()

def validate():
    if len(sys.argv)<3:
        sys.exit("Too few command line arguments")
    if len(sys.argv)>3:
        