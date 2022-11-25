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
    if "regular.csv" in sys.argv[1]:
        with open("regular.csv" , "r") as file:
            tab=csv.DictReader(file , fieldnames=["name" , "small" , "large"])
            # for t in tab:
            #     print(t["name"] , t["small"] , t["large"])
            print(tabulate(tab,headers="firstrow", tablefmt="grid"))
    if "sicilian.csv" in sys.argv[1]:
        with open("regular.csv" , "r") as file:
            tab=csv.DictReader(file , fieldnames=["name" , "small" , "large"])
            # for t in tab:
            #     print(t["name"] , t["small"] , t["large"])
            print(tabulate(tab,headers="firstrow", tablefmt="grid"))

if __name__=="__main__":
    main()


