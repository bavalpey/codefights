"""
Remove a part of a given array between given 0-based indexes l and r (inclusive).

Example

For inputArray = [2, 3, 2, 3, 4, 5], l = 2 and r = 4, the output should be
  removeArrayPart(inputArray, l, r) = [2, 3, 5].
"""
def removeArrayPart(a, l, r):
    return a[:l] + a[r+1:]
