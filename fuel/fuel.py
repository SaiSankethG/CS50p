def main():
        fuel=input("Fraction: ")
        f=convert(fuel)
        per=gauge(f)
        print(per)


def convert(fraction):
    while True:
        try:
            num , den=fraction.split("/")
            x=int(num)
            y=int(den)
            f=x/y
            if f<=1:
                return f
        except(ValueError ,EOFError):
            continue

def gauge(f):
    per=int(f*100)
    if per<=1 :
        return "E"
    elif 99<=per:
        return("F")
    else:
        return(f"{per}%")

if __name__=="__main__":
    main()

