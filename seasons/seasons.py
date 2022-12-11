from datetime import date
import sys
import inflect

p=inflect.engine()


def main():
    user_date=input("Enter the date:")
    minutes=convert(user_date)
    print(f"{p.number_to_words(minutes), andword=""} minutes")

def convert(user_date):
    try:
        b=date.fromisoformat(user_date)
    except:
        sys.exit("Invalid Date")
    today=date.today()
    sub=today-b
    day=sub.days
    total_minutes=day*1440
    return round(total_minutes)



...


if __name__ == "__main__":
    main()