import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    if ".csv" in sys.argv[1]:
        table()

def table():
    if "regular.csv" in sys.argv[1]:
        open("regular.csv" , "r") as file:
            tab=csv.DictWriter(file , fieldnames=["name" , "small" , "large"])
            print(tabulate(tab , header , tablefmt="grid"))



