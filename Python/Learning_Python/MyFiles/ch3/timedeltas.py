from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta     # time delta is a span of time, use for performing time based mathematics

def main():
    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date
    now = datetime.now()
    print("today is: " + str(now))

    print("one year from now it will be: " + str(now + timedelta(days=365)))
    print("180 days from now it will be: " + str(now + timedelta(days=180)))

    # more than one arg
    print("In 2 days and 3 weeks, it will be " +
        str(now + timedelta(days=2, weeks=3)))

    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: " + s)


    ### How many days until April Fools' Day?
    today = date.today()
    afd = date(today.year, 4, 1)
    # Check if april fools has already passed
    if afd < today: # can compare dates to each other
        print("April Fool's day already went by %d days ago" % ((today-afd).days))
        afd = afd.replace(year = today.year+1) # calculate next years april fools day
    
    # Calculate amount of time until April fools day
    time_to_afd = afd-today
    print("It's just", time_to_afd.days, "days until April Fool's Day")

    
if __name__ == "__main__":
    main()