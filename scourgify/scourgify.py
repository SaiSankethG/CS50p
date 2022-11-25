import csv
import sys

def main():
    command_line_arguments()
    try:
        with open(sys.argv[1] , "r") as file:
            write=csv.DictReader(file)
            for w in write:
                print(w)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def command_line_arguments():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] and sys.argv[2]:
        sys.exit("Not a csv file")

if __name__=="__main__":
    main()
