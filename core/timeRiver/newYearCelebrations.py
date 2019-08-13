"""
You're a pretty busy billionaire, and you often fly your personal Private Jet to remote places. Usually travel doesn't bother
you, but this time you are unlucky: it's New Year's Eve, and since you have to fly halfway around the world, you'll probably
have to celebrate New Year's Day in mid-air!

Your course lies west of your current location and crosses several time zones. The pilot told you the exact schedule: it is
known that you will take off at takeOffTime, and in minutes[i] after takeoff you will cross the ith border between time
zones. After crossing each border you will have to set your wrist watch one hour earlier (every second matters to you, so you
can't let your watch show incorrect time). It is guaranteed that you won't cross the IDL (i.e. after crossing each time zone
border your current time will be set one hour back).

You've been thinking about this situation and realized that it might be a good opportunity to celebrate New Year's Day more
than once, i.e. each time your wrist watch shows 00:00. Assuming that you set your watch immediately after the border is
crossed, how many times will you be able to celebrate this New Year's Day with a nice bottle of champagne? Note that the
answer should include celebrations both in mid-air and on the ground (it doesn't matter if the plane landed in the last time
zone before the midnight or not, you'll not let the last opportunity to celebrate New Year slip through your fingers).
"""

from datetime import datetime
from datetime import timedelta
def newYearCelebrations(takeOffTime, minutes):
  takeOff = datetime.strptime(f"{takeOffTime} 12 31 2019", "%H:%M %m %d %Y")
  newYear = datetime.strptime(f"00:00 1 01 2020", "%H:%M %m %d %Y")
  if takeOff.minute == 0 and takeOff.hour== 0:
    takeOff = newYear
  deltas = [timedelta(minutes=i - minutes[p-1]) if p > 0 else timedelta(minutes = i) for p, i in enumerate(minutes)]
  addHr = timedelta(hours=-1)
  cnt = 0
  
  for pos, d in enumerate(deltas, 1):
    if takeOff <= newYear and (takeOff + d >= newYear):
      cnt += 1
      # print("Celebrated new year!")
    takeOff = takeOff + timedelta(hours=-1) + d

  if takeOff <= newYear:
    cnt +=1
  return cnt
