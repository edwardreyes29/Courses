import calendar

# create plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) # SUNDAY will be set as first day of the week
st = c.formatmonth(2020, 4, 0, 0)
print(st)

# html formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2020, 4)
# print(st)

for i in c.itermonthdays(2020,8): # year, month
    print(i) # each day of the month | 0 indicate days that belonged to another month

# for name in calendar.month_name:
#     print(name)
# print()
# for day in calendar.day_name:
#     print(day)
# print()

# Team met on first firday of every month, write script that will write what those dates would be
# calculate the first firday of each month and calcuate the date that represents that day

print("Team meetings will be on: ")
for m in range(1,13): # 13 non inclusive in the range
    cal = calendar.monthcalendar(2020, m) # get an array of weeks that represnet days of the month
    """ the first friday has to be within the first 2 weeks """
    weekone=cal[0] # week 1
    weektwo=cal[1] # week 2

    if weekone[calendar.FRIDAY] != 0:   # means day is part of a different month ^^^
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
