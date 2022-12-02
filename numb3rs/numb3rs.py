import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" , ip):
        list_of_numbers=ip.split(".")
        if list_of_numbers in range(255):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()