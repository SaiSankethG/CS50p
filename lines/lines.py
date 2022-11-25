import sys
def main():
    try:
        if len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        if len(sys.argv)>2:
            print("Too many command-line arguments")
            sys.exit(0)
        if ".py" not in sys.argv[1]:
            sys.exit("Not a python file")
        if ".py" in sys.argv[1]:
            lines_of_code()
    except FileNotFoundError:
        print("File not Found")
        sys.exit(0)

def lines_of_code():
    with open(sys.argv[1] , "r") as file:

if __name__=="__main__":
    main()