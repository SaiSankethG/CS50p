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
    try:
        date=input("Date:")
        m ,d , y=date.split(" ")
        if m in month:
            if d>31:
                continue
            else:
                print(f"{y}-{m}-{d}")
    except