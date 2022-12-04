import re
import sys


def main():
    print(count(input("Text: ")))
    sys.exit(0)


def count(s):
    all_um = re.findall(r"\bum\b", s ,re.IGNORECASE)
    #print(all_um)
    return len(all_um)

if __name__ == "__main__":
    main()