month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date=input("Date:").title()
    try:
        m,d,y=date.split("/")
        if (1>=int(m)<=12 and 1>=int(d)<=31):
            break
    except:
        try:
            m1 , d1,  y=date.split(" ")
            for i in range(len(month)):
                if m1==month:
                    m=i
            d=d1.replace("," , "")
            if (1>=int(m)<=12 and 1>=int(d)<=31):
                break
        except EOFError:
            print()
            pass

print(f"{y}-{int(m):02}-{int(d):02}")