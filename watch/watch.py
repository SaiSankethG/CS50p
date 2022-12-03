import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    li=list(s.split(" "))
    #print(url)
    if "src" in li:
        url=li.split("=")
        print(url)



if __name__ == "__main__":
    main()