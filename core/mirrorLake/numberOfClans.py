"""
Let's call two integers A and B friends if each integer from the array divisors is either a divisor of both A and B or neither A nor B.
If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?

Example

For divisors = [2, 3] and k = 6, the output should be
numberOfClans(divisors, k) = 4.

The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a clan, and 3 and 6 do not have friends and each is a clan
by itself. So the numbers 1 through 6 are broken into 4 clans.
"""
def numberOfClans(divisors, k):
    y = []
    for x in range(1,k+1):
        j = list(bool(x%divisor) for divisor in divisors)
        if j not in y:
            y.append(j)
    return len(y)
