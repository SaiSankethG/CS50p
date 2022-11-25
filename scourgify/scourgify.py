import csv
import sys

def main():
    command_line_arguments()
    try:
        

def command_line_arguments():
    if len(sys.argv)<1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")
