def main():
        fuel=input("Fraction: ")
        f=convert(fuel)
        gauge(f)



def convert(fraction):
        num , den=fraction.split("/")
        x=int(num)
        y=int(den)
        f=x/y
        if f<=1:
            return f

def gauge(f):
    per=int(f*100)
    if per<=1 :
        print("E")
    elif 99<=per:
        print("F")
    else:
        print(f"{per}%")
if __name__=="__main__":
    main()

