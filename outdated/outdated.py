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
        month , day, year=date.split("/")
        if 1<=int(month)<=12 and 1<=int(day)<=31:
            pass
        else:
            break
    elif "," in date:
        month , o_day, year=date.split(",")
        day=o_day.replace("," , "")
        