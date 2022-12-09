from datetime import date
import inflect


class no_of_minutes:
    def __init__(self , user_date):
        user_calendare
        user_calendar=date.isocalendar(user_date)
        print(user_calendar)


        #print(year, month , day)
    #def __sub__(self ,other):




def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        date_of_birth=no_of_minutes(user_date)
        today=no_of_minutes(date.today())


    except ValueError:
        print("Invalid date")


...


if __name__ == "__main__":
    main()