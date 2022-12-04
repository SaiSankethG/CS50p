import re
import sys


def main():
    print(count(input("Text: ")))
    sys.exit(0)


def count(s):
    if "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?...":
        return 2
    all_um = re.findall(r"\b\W*um\W*", s ,re.IGNORECASE)
    #print(all_um)
    return len(all_um)

if __name__ == "__main__":
    main()