"""
Given an integer n, find the minimal k such that
  k = m! (where m! = 1 * 2 * ... * m) for some integer m;
  k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
Guaranteed constraints:
1 ≤ n ≤ 120.
"""
def leastFactorial(n):
    total = 1
    count = 0
    while(n > total):
        total *= (count+1)
        if not (n>total):
            return total
        count+=1
    return total
