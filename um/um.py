import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.compile("um ")
    count_um = 0
    for u in um.findall(s):
        if u == "um":
            count_um += 1
    return count_um

if __name__ == "__main__":
    main()