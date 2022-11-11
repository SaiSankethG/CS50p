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
            break
    except:
        try:
            
        pass