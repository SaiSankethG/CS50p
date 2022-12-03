import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try :
        if re.search(r"^([0-9]\.[0-9][0-9])(.*to.*)([0-9]\.[0-9][0-9]).*$" , s):
            
    except ValueError:
        print("It is not valid")



if __name__ == "__main__":
    main()