from datetime import datetime

def check_todays_date():
    today = datetime.today()
    print("Today's date is:", today.strftime('%Y-%m-%d'))

if __name__ == "__main__":
    check_todays_date()