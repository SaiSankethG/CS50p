import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url=list(s.split(" "))
    print(url)

if __name__ == "__main__":
    main()