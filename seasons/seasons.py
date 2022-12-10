from datetime import date
import inflect


class no_of_minutes:
    def __init__(self , user_date):
        self.userdate=user_date
    def convert_minutes(self):
        year,month, day=self.userdate.split("-")
        return list(date(int(year) , int(month) , int(day)).isocalendar())



def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        user_minutes=no_of_minutes(user_date)
        user_calendar=user_minutes.convert_minutes()
        print(user_calendar)
        today=[]
        today.append(date.today().year)
        today.append(date.today().month)
        today.append(date.today().day)
        print(today)
        print(list(date(int(date.today().year), int(date.today().month) , int(date.today().day)).isocalendar()))
        #print(date(today).isocalendar())
        # today_minutes=no_of_minutes(today)
        # today_calendar=today_minutes.convert_minutes()
        # print(today_calendar)


    except ValueError:
        print("Invalid date")



...


if __name__ == "__main__":
    main()