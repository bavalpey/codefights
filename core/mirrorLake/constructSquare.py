"""
Given a string consisting of lowercase English letters, find the largest square number which can be obtained by reordering the string's
characters and replacing them with any digits you need (leading zeros are not allowed) where same characters always map to the same
digits and different characters always map to different digits.

If there is no solution, return -1.

Example

  For s = "ab", the output should be
    constructSquare(s) = 81.
  The largest 2-digit square number with different digits is 81.
  For s = "zzz", the output should be
    constructSquare(s) = -1.
  There are no 3-digit square numbers with identical digits.
  For s = "aba", the output should be
    constructSquare(s) = 900.
  It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.
  
Guaranteed constraints:
  1 ≤ s.length < 10.
"""
def constructSquare(s):
    val = freq(s)
    lowerbound = [1, 4, 10, 32, 100, 317, 1000, 3163, 10000, 31623]
    upperbound = [3, 9, 31, 99, 316, 999, 3162, 9999, 31622, 99999]
    for x in range(lowerbound[len(s)-1],upperbound[len(s)-1]+1)[::-1]:
        if freq(x*x) == val:
            return x*x
    return -1
def freq(x):
    x = str(x)
    a = []
    for i in set(x):
        a.append(x.count(i))
    return sorted(a)
