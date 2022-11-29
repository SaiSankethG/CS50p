import sys
from PIL import Image, ImageOps
from os.path import splitext
def main():
    validate()
    try:
        PIL.Image.open(sys.argv[1], mode="r", formats=None)
    except:
        print()

def validate():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")           #check for less than three commands.
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")          #check for more than three commands.
    file1=splitext(sys.argv[1])                              #splitext(it will split the text and stores as list) and store in file1 and file2
    file2=splitext(sys.argv[2])
    # print(file1)
    # print(file2)
    # if ".png"and".jpg"and".jpeg" not in sys.argv[1] and sys.argv[2]:
    #     sys.exit("Invalid input")
    # if sys.argv[1].split(".") != sys.argv[2].split("."):
    #     sys.exit("Input and output have different extensions")
    if check(file1)==False:                                         #if the first file has no extension in the list then it will return invalid input
        sys.exit("Invalid input")
    if check(file2)==False:                                         #same
        sys.exit("Invalid input")
    if file1[1].lower()!= file2[1].lower():
        sys.exit("Input and output have different extensions")      #if both the file has different extension.

def check(file):
    if file[1] in [".png" , ".jpg" , ".jpeg"]:
        return True
    return False
if __name__=="__main__":
    main()