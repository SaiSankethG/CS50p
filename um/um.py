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
    um=re.findall( r"[^a-z]um[^a-z]" , s)
    print(um)
    # for all_um in um:
    #     if all_um == "um":


if __name__ == "__main__":
    main()