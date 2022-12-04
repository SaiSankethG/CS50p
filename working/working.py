import re
import sys


def main():
    convert(input("Hours: "))


def convert(s):
    if user_input:=re.search(r"^([0-9]+)\:?([0-9]+)?\ (PM|AM)\ to\ ([0-9]+)\:?([0-9]+)?\ (AM|PM)$", s):
        time=list(user_input.groups())
        #print(time)
        if int(time[0])<12 and int(time[3])<12:
            if time[1]==None:
                time[1]="00"
                time[4]="00"
                #print(time[1] , time[4])
            if 0<=int(time[1])<60 and 0<=int(time[4])<60:
                if time[2] == "AM" or "PM":
                    if time[2] == "AM":
                        n=int(time[0])
                        print(f"{n:02}", f":{time[1]}" , " to " ,sep='' , end='')
                    elif time[2] == "PM":
                        time[0]=int(time[0])+12
                        print(time[0] , f":{time[1]}" , " to " , sep='' , end='')
                if time[5]==  "AM" or "PM":
                    if time[5] == "AM":
                        m=int(time[3])
                        print(f"{m:02}" ,f":{time[4]}",sep='')
                    elif time[5] == "PM":
                        time[3]=int(time[3])+12
                        print(time[3] , f":{time[4]}" , sep='')
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()