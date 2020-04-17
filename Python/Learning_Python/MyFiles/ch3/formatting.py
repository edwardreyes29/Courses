#
# Formatting time and date output
#

from datetime import datetime

def main():
    now = datetime.now()

    # %y/%Y - Year,  %a/%A - Weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y")) # strftime(), %Y is a placeholder for year
    print(now.strftime("%a, %d, %B, %y"))

    # local specific information: %c - locale's data and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    # time formatting: %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p")) 
    print(now.strftime("Current time: %H:%M")) # 24 hour clock


if __name__ == "__main__":
    main()

# %d-%b-%Y %H:%M:$S -> 13-Mar-2020 16:42:58
