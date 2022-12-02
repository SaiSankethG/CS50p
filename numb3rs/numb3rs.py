import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches:=re.match(r"^[0-255]\.[0-255]\.[0-255]\.[0-255]$" , ip):
        return True
    return False



if __name__ == "__main__":
    main()