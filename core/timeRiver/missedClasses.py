"""
Your Math teacher takes education very seriously, and hates it when a class is missed or canceled for any reason. He even made
up the following rule: if a class is missed because of a holiday, the teacher will compensate for it with a makeup class after
school.

You're given an array, daysOfTheWeek, with the weekdays on which your teacher's classes are scheduled, and holidays,
representing the dates of the holidays throughout the academic year (from 1st of September in year to 31st of May in year+1).
How many times will you be forced to stay after school for a makeup class because of holiday conflicts in the current academic
year?

For your convenience, here is the list of month lengths (from January to December, respectively):

  Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
  
Please note that in leap years February has 29 days.

Example

For year = 2015, daysOfTheWeek = [2, 3], and
holidays = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"],
the output should be
  missedClasses(year, daysOfTheWeek, holidays) = 3.
"""

from datetime import datetime
def missedClasses(year, daysOfTheWeek, holidays):
  days = [datetime.strptime(f"{h}-{year+1}", "%m-%d-%Y").weekday() + 1 if int(h[:2]) <=5
            else datetime.strptime(f"{h}-{year}", "%m-%d-%Y").weekday() + 1 for h in holidays]
  return len([day for day in days if day in daysOfTheWeek])
  
