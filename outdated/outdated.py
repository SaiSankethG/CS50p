months = [
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
    "December",
]
while True:
    date=input("date:")
    if "/" in date:
        if int(month)>12 and int(day)>31:
            pass
        else:
            month , day ,year=date.split("/")
            break
    elif "," in date:
        date=date.replace("," , "")
        month, day, year=date.split(" ")
        if month in months:
            month=months.index(month)+1
            if int(month)>12 and int(day)>31:
                pass
            else:
                break

print(f"{int(year)}-{int(month):02}-{int(day):02}")
