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
        month , day , o_year=date.split("/")
        year=o_year.replace(" " , "")
        if (1<=int(month)<=12 and 1<=int(day)<=31):
            break
    except:
        try:
            month,d1,y=date.split(" ")
            for i in range(len(month)):
                if m1==month:
                    m=i
            d=d1.replace("," , "")
            if (1<=int(m)<=12 and 1<=int(d)<=31):
                break
        except EOFError:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")