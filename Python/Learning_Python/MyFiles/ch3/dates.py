#
#   Example file for working with date information
#

# from datetime module, import date, time, and datetime classes
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # date
    # today = date.today()
    # print("Today's date is ", today)

    # print("Date components", today.day, today.month, today.year)

    # print("Today's weekday # is:", today.weekday())
    # days = ["mon", "tue", "wed", "thur", "fri","sat","sun"]
    # print("Which is a:", days [today.weekday()])

    # datetime
    today = datetime.now()
    print("The current date time is", today)

    t = datetime.time(datetime.now())
    print("Time:",t)

if __name__ == "__main__":
    main()