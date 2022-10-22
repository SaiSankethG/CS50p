 def main():
    time=input("Whats the time?")
    hours , minutes=convert(time)
    if hours>=7 and hours+minutes<=8:
       print("Breakfast time")
    elif hours>=12 and hours+minutes<=13:
       print("Breakfast time")
    elif hours>=7 and hours+minutes<=8:
       print("Breakfast time")



def convert(time):
    return hours , minutes =time.split(":")

if __name__ == "__main__":
    main()