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
        m, d,y=date.split("/")
        if (1>=int(m)<=12 and 1>=int(d)<=31):
            print(f"{y}-{int(m):02}-{int(d):02}")
            break
    except:
        try:
            m1 , d1,  y1=date.split(" ")
            for i in range(len(month)):
                if m1==month:
                    m2=i
            d2=d1.replace("," , "")
            if (1>=int(m2)<=12 and 1>=int(d2)<=31):
                print(f"{y1}-{int(m2):02}-{int(d2):02}")
                break
        except EOFError:
            print()
            pass

