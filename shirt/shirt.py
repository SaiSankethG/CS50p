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
    file1=splitext(sys.argv[1])
    file2=splitext(sys.argv[2])
    # if ".png"and".jpg"and".jpeg" not in sys.argv[1] and sys.argv[2]:
    #     sys.exit("Invalid input")
    # if sys.argv[1].split(".") != sys.argv[2].split("."):
    #     sys.exit("Input and output have different extensions")
    if check(file1)==False:
        sys.exit("Invalid input")
    if check(file2)==False:
        sys.exit("Invalid input")
    if file1[1].lower()!= file2[1].lower():
        sys.exit("Input and output have different extensions")

def check(file):
    if file in [".png" , ".jpg" , ".jpeg"]:
        return True
    return False
    retur
if __name__=="__main__":
    main()