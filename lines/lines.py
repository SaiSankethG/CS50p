import sys
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        print("Too many command-line arguments")
        sys.exit(0)
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    if ".py" in sys.argv[1]:
        lines_of_code()


def lines_of_code():
    try:
        with open(sys.argv[1] , "r") as file:
            lines=file.readlines()
            count=0
            for line in lines:
                if line.isspace() == True:
                    pass
                elif line.lstrip().startswith("#")==True:
                    pass
                else:
                    count+=1
            print(count)
    except FileNotFoundError:
        sys.exit("File not Found")

if __name__=="__main__":
    main()