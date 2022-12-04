import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # um = re.compile(r"um[^\w]+")
    # count_um = 0
    # for u in um.finditer(s):
    #     if u == "um":
    #         count_um += 1
    # return count_um
    um=re.findall( r"um[^\w]*" , s)
    count=0
    print(um)

if __name__ == "__main__":
    main()