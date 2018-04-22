"""
You decided to create a malicious program to play a joke on your friend. He's now struggling with a report for his work, and you want to
scare him by spoiling some dates in it (of course you will change them back after you have your moment of joy). However, you don't want
him to discover the errors until he starts double-checking the report, so all spoiled dates should be valid.

Now your goal is to write a program that modifies the curDate according to the rules that specify the changes that should be made.
However, if the changes result in an incorrect date, the program should leave the date as is.

Given the changes and the curDate, return the spoiled date or don't change it if the result appears to be invalid.

Example

  For curDate = "01 Jul 2016 16:53:24" and
    changes = [2, 3, -1, 0, 5, 4], the output should be
    maliciousProgram(curDate, changes) = "03 Oct 2015 16:58:28";

  For curDate = "15 Mar 1998 12:09:59" and
    changes = [-2, 0, 9, 1, 3, 1], the output should be
    maliciousProgram(curDate, changes) = "15 Mar 1998 12:09:59".
    
  After changing the date will look like "13 Mar 2007 13:12:60", which is incorrect, because the number of seconds cannot be equal to 60.
"""
from datetime import datetime as dt
import time
def maliciousProgram(curDate, changes):
    this = dt.strptime(curDate, "%d %b %Y %H:%M:%S")
    print(type(this.hour))
    try:
        answer = this.replace(year=this.year+changes[2], month=this.month+changes[1], day=this.day+changes[0],
                              hour=this.hour+changes[3],minute=this.minute+changes[4], second=this.second+changes[5])
        return answer.strftime("%d %b %Y %H:%M:%S")
    except ValueError:
        return this.strftime("%d %b %Y %H:%M:%S")
