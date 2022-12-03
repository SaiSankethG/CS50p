import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url=re.sub(r"https://www.youtube.com/embed/" , r"https://youtu.be/",s)
    for u in url:
        if "youtu.be" in u:
            print(u)

if __name__ == "__main__":
    main()