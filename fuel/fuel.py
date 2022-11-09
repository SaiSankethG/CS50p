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

per=f*100
if 0<per<1 :
    print("E")
elif 99<per<=100:
    print("F")
else:
    print(f"{per}%")


