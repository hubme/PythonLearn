import calendar
import datetime

def findDay(date):
    born = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return calendar.day_name[born]

date = "05 05 2020"
print(findDay(date))