"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
  alphabeticShift(inputString) = "dsbaz".
"""
def alphabeticShift(inputString):
    old_a = 'abcdefghijklmnopqrstuvwxyz'
    new_a = 'bcdefghijklmnopqrstuvwxyza'
    new_str = ""
    for i,c in enumerate(inputString):
        index = old_a.find(c)
        new_str += (new_a[index])
    return new_str
