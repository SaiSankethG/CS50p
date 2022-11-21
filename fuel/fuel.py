def main():
    


def convert(fraction)
while True:
    fuel=input("Fraction: ")
    try:
        num , den=fuel.split("/")
        x=int(num)
        y=int(den)
        f=x/y
        if f<=1:
            break
    except(ValueError , ZeroDivisionError):
        continue

per=int(f*100)
if per<=1 :
    print("E")
elif 99<=per:
    print("F")
else:
    print(f"{per}%")


