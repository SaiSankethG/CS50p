x=int(input("Score:"))

if 90<=x<=100:
    print("A")
elif 80<=x<90:
    print("B")
elif x>=70 and x<80:
    print("C")
elif x>=60 and x<70:
    print("D")
else:
    print("F")