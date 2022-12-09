from datetime import date
import inflect


class no_of_minutes:
    def __init__(self , user_date):
        self.user_date=user_date
        return self.user_date




def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        date_of_birth=no_of_minutes(date.isocalendar(user_date))
        print(date_of_birth)
        today_date=date.today()
        today=no_of_minutes(date.isocalendar(today_date))
        print(today)


    except ValueError:
        print("Invalid date")


...


if __name__ == "__main__":
    main()