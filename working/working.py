import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # try :
    #     if re.search(r"^([0-9]\.[0-9][0-9])(.*to.*)([0-9]\.[0-9][0-9]).*$" , s):
    #         if
    # except ValueError:
    #     print("It is not valid")
    #def convert(time):
    hour, minute, meridian = time.split(" ")
    hour = int(hour)
    if meridian == "PM" and hour != 12:
        hour += 12
    elif meridian == "AM" and hour == 12:
        hour = 0
    return "{:02d}:{:02d}".format(hour, int(minute))



if __name__ == "__main__":
    main()