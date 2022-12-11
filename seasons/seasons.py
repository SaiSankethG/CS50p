from datetime import date
import sys

def main():
    user_date=input("Enter the date:")
    minutes=convert(user_date)

def convert(user_date):
    try:
        b=date.fromisoformat(user_date)
    except:
        sys.exit("Invalid Date")
    today=date.today()
    days=today-b
    minutes=days.total


...


if __name__ == "__main__":
    main()