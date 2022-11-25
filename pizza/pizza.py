import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    if ".csv" in sys.argv[1]:
        table()

def table():
    try:
        if "regular.csv" in sys.argv[1]:
            with open("regular.csv" , "r") as file:
                tab=csv.DictReader(file , fieldnames=["name" , "small" , "large"])
                sys.exit(tabulate(tab,headers="firstrow", tablefmt="grid"))
        if "sicilian.csv" in sys.argv[1]:
            with open("sicilian.csv" , "r") as file:
                tab=csv.DictReader(file , fieldnames=["name" , "small" , "large"])
                sys.exit(tabulate(tab,headers="firstrow", tablefmt="grid"))
        if "regular" and "sicilian" not in sys.argv[1]:
            sys.exit("File does not exist")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__=="__main__":
    main()


