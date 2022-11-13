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
        month , day ,year=date.split("/")
    elif "," in date:
        date=date.replace("," , "")
        month, day, year=date.split(" ")

print(f"")
