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
        date=input("Date:").title()
        m,d=date.split(" ")
        if m in month:
            if d>31:
                continue
            else:
                print(f"{y}-{m}-{d}")
    except (EOFError , ValueError):
        pass
    else:
        print("Not valid")