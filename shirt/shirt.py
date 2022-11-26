import sys
# from PIL import image
def main():
    validate()
    # try:


def validate():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".png"and".jpg"and".jpeg" not in sys.argv[1] and sys.argv[2]:
        sys.exit("Invalid input")
    if sys.argv[1].split(".") != sys.argv[2].split("."):
        sys.exit("Input and output have different extensions")
if __name__=="__main__":
    main()