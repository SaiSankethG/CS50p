import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe.*><\/iframe>" , s):
        url=re.search(r"https?:\/\/(www\.)?youtube\.com\/embed\/[A-Za-z0-9]+" ,s)
        if url:





if __name__ == "__main__":
    main()