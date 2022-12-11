from datetime import date
import sys
import inflect

p=inflect.engine()


def main():
    user_date=input("Date of Birth:")
    print(convert(user_date))

def convert(user_date):
    try:
        b=date.fromisoformat(user_date)
    except:
        sys.exit("Invalid Date")
    today=date.today()
    sub=today-b
    day=sub.days
    total_minutes=day*1440
    return (f"{p.number_to_words(total_minutes, andword='')} minutes")


if __name__ == "__main__":
    main()