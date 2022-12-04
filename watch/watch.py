import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if user_input:=re.search(r"^([0-9]+)(\:[0-9]+)?\ (AM|PM)\ to\ ([0-9]+)(\:[0-9]+)?\ (AM|PM)$", s):
            time=list(user_input.groups())
            # print(time)
            # print(time[0])
            time[1]=":00"
            time[4]=":00"
            if time[2] == "AM" or "PM":
                if time[2] == "AM":
                    
                    print(f"{time[0]:02}" , time[1] , " to " ,sep='' , end='')
                elif time[2] == "PM":
                    time[0]=int(time[0])+12
                    print(time[0] , time[1] , " to " , sep='' , end='')
            if time[5]==  "AM" or "PM":
                if time[5] == "AM":
                    print(f"{time[3]:02}" , time[4],sep='')
                elif time[5] == "PM":
                    time[3]=int(time[3])+12
                    print(time[3] , time[4] , sep='')
    except ValueError:
        print("It is not valid")

if __name__ == "__main__":
    main()