"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the
strings at consecutive positions would differ by exactly one character.

Example

  For inputArray = ["aba", "bbb", "bab"], the output should be
    stringsRearrangement(inputArray) = false;

  All rearrangements don't satisfy the description condition.

  For inputArray = ["ab", "bb", "aa"], the output should be
    stringsRearrangement(inputArray) = true.

  Strings can be rearranged in the following way: "aa", "ab", "bb".
"""
from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False
