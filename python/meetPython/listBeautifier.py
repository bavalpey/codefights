"""
Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, your task is to
chop off its first and its last element until it becomes beautiful. Implement a function that will make the given a beautiful as
described, and return the resulting list as an answer.

Example

  For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be
    listBeautifier(a) = [4, 38, 4].
  Here's how the answer is obtained:
    [3, 4, 2, 4, 38, 4, 5, 3, 2] => [4, 2, 4, 38, 4, 5, 3] => [2, 4, 38, 4, 5] => [4, 38, 4].

  For a = [1, 4, -5], the output should be
    listBeautifier(a) = [4].
"""
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res = res[1:-1]# = res
    return res
