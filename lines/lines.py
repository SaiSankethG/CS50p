import sys

try:
    if sys.argv[1]==0:
        print("Too few command-line arguments")
        sys.exit(0)
    elif len(sys.argv)>2:
        print("Too many command-line arguments")
        sys.exit(0)
    elif ".py" not in sys.argv[1]:
        print("Not a python file")
        sys.exit(0)
    elif ".py" not in sys.argv[1]:
        lines_of_code()
except FileNotFoundError:
    print("File not Found")
    sys.exit(0)

def lines_of_code():
    print()