import sys
def main():
    try:
        try:
            if sys.argv[0]==0:
                print(end="")
        except IndexError:
            print("Too few command-line arguments")
            sys.exit(0)
        if len(sys.argv)>2:
            print("Too many command-line arguments")
            sys.exit(0)
        elif ".py" not in sys.argv[1]:
            print("Not a python file")
            sys.exit(0)
        elif ".py" in sys.argv[1]:
            lines_of_code()
    except FileNotFoundError:
        print("File not Found")
        sys.exit(0)

def lines_of_code():
    print("hello")
main()