"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
  palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""
def palindromeRearranging(inputString):
    d = {}
    for i in inputString:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    total = 0
    for i in d:
        print(d[i])
        if total > 1:
            return False
        if d[i] %2 != 0 and len(inputString) % 2 == 0:
            return False
        if d[i] % 2 != 0:
            total += 1
    return True
