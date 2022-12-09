from datetime import date
import inflect


class no_of_minutes:
    def __init__(self , user_date):
        self.userdate=user_date
    def convert_minutes(self):
        year,month, day=self.userdate.split("-")
        return date(int(year) , int(month) , int(day)).isocalendar()



def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        user_minutes=no_of_minutes(user_date)
        user_calendar=user_minutes.convert_minutes()
        print(user_calendar)
        today=date.today()
        print(today)
        #print(date(today).isocalendar())
        # today_minutes=no_of_minutes(today)
        # today_calendar=today_minutes.convert_minutes()
        # print(today_calendar)


    except ValueError:
        print("Invalid date")



...


if __name__ == "__main__":
    main()