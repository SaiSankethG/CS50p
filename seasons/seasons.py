from datetime import date
import inflect


class no_of_minutes:
    #created a init method to access the year, month, day
    def __init__(self , year , month , day):
        self.year=year
        self.month=month
        self.day=day

    def convert_minutes(self):
        return list(date(int(self.year) , int(self.month) , int(self.day)).isocalendar())

    def __sub__(self , other):
        year=self.year-int(other.year)
        month=self.month-int(other.month)
        day=self.day-int(other.day)
        return no_of_minutes(year ,month, day)


def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        year,month, day=user_date.split("-")

        #passing the user input date
        user_minutes=no_of_minutes(year, month, day)
        user_calendar=user_minutes.convert_minutes()
        print(user_calendar)

        #passing the present day
        today_minutes=no_of_minutes(int(date.today().year), int(date.today().month) , int(date.today().day))
        today_calendar=today_minutes.convert_minutes()
        print(today_calendar)

        #different in days , months, years
        diff_date=today_minutes-user_minutes
        #print(diff_date.convert_minutes())
        


    except ValueError:
        print("Invalid date")



...


if __name__ == "__main__":
    main()