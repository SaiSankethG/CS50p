import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    all_um = re.findall(r"\b\W*um\W*", s ,re.IGNORECASE)
    #print(all_um)
    return len(all_um)

if __name__ == "__main__":
    main()