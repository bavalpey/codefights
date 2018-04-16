"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

  For n = 9, the output should be
    isSumOfConsecutive2(n) = 2.

  There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

  For n = 8, the output should be
    isSumOfConsecutive2(n) = 0.

  There are no ways to represent n = 8.

Guaranteed constraints:
  1 ≤ n ≤ 25.
"""
def isSumOfConsecutive2(n):
    result = 0;
    for start in range(1,n):
        number = n
        subtrahend = start
        while (number > 0):
            number -= subtrahend
            subtrahend += 1
        if (number==0):
            result += 1
    return result
