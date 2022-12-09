from datetime import date
import inflect


class no_of_minutes:
    def __init__(self , user_date):
        self.userdate=user_date



def main():
    user_date=input("Date of Birth: ")
    try:
        date.fromisoformat(user_date)
        user_minutes=no_of_minutes(user_date)



    except ValueError:
        print("Invalid date")



...


if __name__ == "__main__":
    main()