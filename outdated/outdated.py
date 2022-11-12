months=[
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
            o_month,o_day,year=date.split(" ")
            for i in range(len(month)):
                if o_month==ynths:
                    month=i
            day=o_day.replace("," , "")
            if (1<=int(month)<=12 and 1<=int(day)<=31):
                break
        except EOFError:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")