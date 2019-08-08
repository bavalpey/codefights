"""
Whenever you decide to celebrate your birthday you always do this your favorite café, which is quite popular and as such
usually very crowded. This year you got lucky: when you and your friend enter the café you're surprised to see that it's
almost empty. The waiter lets slip that there are always very few people on this day of the week.

You enjoyed having the café all to yourself, and are now curious about the next time you'll be this lucky. Given the current
birthdayDate, determine the number of years until it will fall on the same day of the week.

For your convenience, here is the list of months lengths (from January to December, respectively):

Months lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
Please, note that in leap years February has 29 days. If your birthday is on the 29th of February, you celebrate it once in
four years. Otherwise you birthday is celebrated each year.

Example

For birthdayDate = "02-01-2016", the output should be
  dayOfWeek(birthdayDate) = 5.

February 1 in 2016 is a Monday. The next year in which this same date will be Monday too is 2021. 2021 - 2016 = 5, which is
the answer.
"""

import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta


def dayOfWeek(birthdayDate):
  start = datetime.strptime(birthdayDate, '%m-%d-%Y').date()
  start_weekday = start.weekday()
  
  end = -1
  
  if start.month == 2 and start.day == 29:
    year_delta = 4
  else:
    year_delta = 1
  cnt = 0
  
  while end != start_weekday:
    cnt += year_delta
    
    if year_delta == 4:
      if calendar.isleap(start.year + 4):
        start = start + relativedelta(years=4)
      else:
        start = start + relativedelta(years=8)
        cnt += 4
    else: start = start + relativedelta(years=1)

    end = start.weekday()
    
  return cnt
