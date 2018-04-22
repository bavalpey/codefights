"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the
digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

  For n = 1230, the output should be
    isLucky(n) = true;
  For n = 239017, the output should be
    isLucky(n) = false.
"""
def isLucky(n):
    l = list(str(n))
    sum1 = sum2 = count = 0
    for num in l:
        if count < len(l)/2:
            sum1 += int(num)
        else:
            sum2 += int(num)
        count += 1
    return sum1 == sum2
