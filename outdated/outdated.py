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
    date=input("Date: ")
    if "/" in date:
        try:
            month , day, year=date.split("/")
            if 1<=int(month)<=12 and 1<=int(day)<=31:
                break
            else:
                pass
        except ValueError:
            pass
    elif "," in date:
        month , o_day, year=date.split(" ")
        day=o_day.replace("," , "")
        if month in months:
            month=months.index(month)+1
            if 1<=int(month)<=12 and 1<=int(day)<=31:
                break
            else:
                pass

print(f"{int(year)}-{int(month):02}-{int(day):02}")